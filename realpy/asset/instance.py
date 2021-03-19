from typing import Type, Union

from ..preset import RsPreset
from ..layer import RsLayer
from ..prefab import RsPrefab, RsInstance


def instance_create(prefab: Type[RsPrefab], layer_id: Union[str, RsLayer], x=0, y=0) -> RsInstance:
    """`instantiate(Scene, Layer, x=0, y=0)`
        ---
        Creates a instance of game object.
    """

    if type(layer_id) is RsLayer:
        TempLayer = layer_id
    else:
        TempLayer = RsPreset.RsRoom.layer_find(str(layer_id))
        if not TempLayer:
            raise RuntimeError("The specific layer are not found.")

    Instance = RsInstance(prefab, RsPreset.RsRoom, TempLayer, x, y)
    Instance.onAwake()
    TempLayer.add(Instance)

    TempHash = hash(prefab)
    try:
        if not RsPreset.RsRoom.SpecificInstancesPot[TempHash]:
            RsPreset.RsRoom.SpecificInstancesPot[TempHash] = []
    except KeyError:
        RsPreset.RsRoom.SpecificInstancesPot[TempHash] = []
    RsPreset.RsRoom.SpecificInstancesPot[TempHash].append(Instance)

    return Instance


def instance_destroy(target):
    target.onDestroy()
    del target
