from typing import Type, Union

from ..preset import RsPreset
from ..layer import RsLayer
from ..prefab import RsPrefab


def instance_create(gobject: Type[RsPrefab], layer_id: Union[str, RsLayer], x=0, y=0):
    if type(layer_id) is RsLayer:
        TempLayer = layer_id
    else:
        TempLayer = RsPreset.RsRoom.layer_find(str(layer_id))
        if not TempLayer:
            raise RuntimeError("The specific layer are not found.")

    Instance = gobject.instantiate(RsPreset.RsRoom, TempLayer, x, y)
    Instance.onAwake()
    TempLayer.add(Instance)

    TempHash = hash(gobject)
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
