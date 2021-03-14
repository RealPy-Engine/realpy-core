from typing import Union

from realpy import preset
from realpy.layer import RsLayer
from realpy.prefab import RsPrefab, RsInstance


def instance_create(gobject: type[RsPrefab], layer_id: Union[str, RsLayer], x=0, y=0) -> RsInstance:
    if type(layer_id) is RsLayer:
        TempLayer = layer_id
    else:
        TempLayer = preset.RsRoom.layer_find(str(layer_id))
        if not TempLayer:
            raise RuntimeError("The specific layer are not found.")

    Instance = gobject.instantiate(preset.RsRoom, TempLayer, x, y)
    Instance.onAwake()
    TempLayer.add_instance(Instance)

    TempHash = hash(gobject)
    try:
        if not preset.RsRoom.SpecificInstancesPot[TempHash]:
            preset.RsRoom.SpecificInstancesPot[TempHash] = []
    except KeyError:
        preset.RsRoom.SpecificInstancesPot[TempHash] = []
    preset.RsRoom.SpecificInstancesPot[TempHash].append(Instance)

    return Instance


def instance_destroy(target: RsInstance):
    target.onDestroy()
    del target
