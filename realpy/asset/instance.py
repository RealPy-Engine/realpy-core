from typing import List, Type, Union

from ..preset import RsPreset
from ..layer import RsLayer
from ..prefab import RsPrefab, RsInstance


def instance_create(prefab: Type[RsPrefab], layer_id: Union[str, RsLayer], x=0, y=0) -> RsInstance:
    """`instance_create(Scene, Layer, x=0, y=0)`
        ---
        Creates an instance of game object.
    """

    if type(layer_id) is RsLayer:
        TempLayer = layer_id
    else:
        try:
            TempLayer = RsPreset.RsRoom.layer_find(str(layer_id))
        except KeyError:
            raise RuntimeError(f"The specific layer '{layer_id}' not found.")

    Instance = RsInstance(prefab, RsPreset.RsRoom, TempLayer, x, y)
    Instance.onAwake()
    TempLayer.add(Instance)

    _instance_register(prefab, Instance)

    return Instance


def _instance_register(prefab: Type[RsPrefab], instance: RsInstance):
    TempHash = hash(prefab)
    Where: List
    try:
        Where = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        RsPreset.RsRoom.SpecificInstancesPot[TempHash] = []
        Where = RsPreset.RsRoom.SpecificInstancesPot[TempHash]

    Where.append(instance)
    RsPreset.RsRoom.EveryInstancesPot.append(instance)

    instance.department.append(Where)
    instance.department.append(RsPreset.RsRoom.EveryInstancesPot)

    Recursive_condition = (issubclass(prefab, RsPrefab) and prefab is not RsPrefab)
    if RsPreset._realpy_debug:
        print(Recursive_condition, "from", prefab)
        print(f"An instance is appended to {Where} of {prefab}.")
    if Recursive_condition:
        _instance_register(prefab.__base__, instance)


def instance_destroy(target: RsInstance):
    target.onDestroy()
    del target
