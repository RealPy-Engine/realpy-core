from typing import List, Optional, Type, Union

from ..preset import RsPreset
from ..layer import RsLayer
from ..prefab import RsPrefab
from ..prefab.instance import RsInstance


def instance_create(prefab: Type[RsPrefab], layer_id: Union[str, RsLayer], x=0, y=0):
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

    Instance = prefab.trait_instance(prefab, RsPreset.RsRoom, TempLayer, x, y)
    Instance.onAwake()
    TempLayer.add(Instance)

    _instance_register(prefab, Instance)

    return Instance


def instance_number(prefab: Type[RsPrefab]) -> int:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        return 0
    return len(Pot)


def instance_find(prefab: Type[RsPrefab], index: int) -> Optional[RsInstance]:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        return None
    return Pot[index]


def _instance_register(prefab: Type[RsPrefab], instance: RsInstance):
    if issubclass(prefab, RsPrefab) and prefab is not RsPrefab:
        RsPreset.RsRoom.EveryInstancesPot.append(instance)
        instance.department.append(RsPreset.RsRoom.EveryInstancesPot)
        _instance_register_recursive(prefab, instance)


def _instance_register_recursive(prefab: Type[RsPrefab], instance: RsInstance):
    TempHash = hash(prefab)
    Where: List
    try:
        Where = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        RsPreset.RsRoom.SpecificInstancesPot[TempHash] = []
        Where = RsPreset.RsRoom.SpecificInstancesPot[TempHash]

    Where.append(instance)
    instance.department.append(Where)

    Recursive_condition = (issubclass(prefab, RsPrefab) and prefab is not RsPrefab)
    if RsPreset.debug_get():
        print(Recursive_condition, "from", prefab)
        print(f"An instance is appended to {Where} of {prefab}.")
    if Recursive_condition:
        print("Goto ", prefab.__base__)
        _instance_register(prefab.__base__, instance)


def instance_destroy(target: RsInstance):
    target.onDestroy()
    del target
