from typing import Union

from realpy import preset
from realpy.layer import RsLayer
from realpy.prefab import RsPrefab, RsInstance


def instance_create(gobject: type[RsPrefab], layer_id: Union[str, RsLayer], x=0, y=0) -> RsInstance:
    if type(layer_id) is RsLayer:
        Temp = layer_id
    else:
        Temp = preset.RsRoom.layer_find(str(layer_id))
        if not Temp:
            raise RuntimeError("The specific layer are not found.")

    Instance = gobject.instantiate(preset.RsRoom, Temp, x, y)
    Instance.onAwake()

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
