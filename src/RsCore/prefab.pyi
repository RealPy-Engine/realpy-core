from typing import Optional, Type

from RsCore.instance import RsObject
from RsCore.sprite import RsSprite


class RsPrefab(object):
    name: str
    __parent: Optional[RsPrefab]
    children: list[RsPrefab]
    link_implement: Type[RsObject]
    sprite_index: Optional[RsSprite]
    serial: int

    def __init__(self, name: str):
        ...

    def __hash__(self) -> int:
        ...

    @property
    def parent(self) -> Optional[RsPrefab]:
        ...

    @parent.setter
    def parent(self, target: Optional[RsPrefab]):
        ...

    def onAwake(self, target):
        ...

    def onDestroy(self, target):
        ...

    def onUpdate(self, time: int, target):
        ...

    def onUpdateLater(self, time: int, target):
        ...

    def onDraw(self, time: int, target):
        ...

    def onGUI(self, time: int, target):
        ...

    ...
