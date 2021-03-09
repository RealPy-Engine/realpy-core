from typing import Optional, Type

from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab


class RsScene(object):
    name: str
    layer_stack: list[RsLayer]
    trees: dict[str, RsLayer]
    paused: bool
    EveryInstancesPot: list
    SpecificInstancesPot: dict[int, list]
    before: Optional[RsScene]
    next: Optional[RsScene]

    def __init__(self, name: str):
        ...

    def __repr__(self) -> str:
        ...

    def add_layer(self, caption: str) -> RsLayer:
        ...

    def layer_find(self, caption: str) -> Optional[RsLayer]:
        ...

    def pause(self):
        ...

    def resume(self):
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
