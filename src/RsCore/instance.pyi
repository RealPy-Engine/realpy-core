from typing import Optional, Type

from RsCore.scene import RsScene
from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.sprite import RsSprite


class RsObject(object):
    link_original: Optional[RsPrefab]
    __enabled: bool
    __visible: bool
    scene: RsScene
    layer: RsLayer
    x: float
    y: float

    def __init__(self, scene: RsScene, layer: RsLayer, x: float = 0, y: float = 0):
        ...

    @property
    def enabled(self) -> bool:
        ...

    @property
    def visible(self) -> bool:
        ...

    @enabled.setter
    def enabled(self, flag: bool):
        ...

    @visible.setter
    def visible(self, flag: bool):
        ...

    def onAwake(self):
        ...

    def onDestroy(self):
        ...

    def onUpdate(self, time: int):
        ...

    def onUpdateLater(self, time: int):
        ...

    def onDraw(self, time: int):
        ...

    def onGUI(self, time: int):
        ...

    ...


class RsDirtyObject(RsObject):
    sprite_index: Optional[RsSprite] = None
    image_angle: float
    image_index: float
    __speed: float
    __direction: float
    __hspeed: float
    __vspeed: float
    gravity: dict[str, float]

    def __init__(self, scene: RsScene, layer: RsLayer, x: float = 0, y: float = 0):
        ...

    ...
