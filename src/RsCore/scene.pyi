from typing import Optional

from RsCore.layer import RsLayer


class RsScene(object):
    name: str
    layer_stack: list[RsLayer]
    trees: dict[str, RsLayer]
    paused: bool
    EveryInstancesPot: list
    SpecificInstancesPot: dict[str, list]
    before: Optional[RsScene] = None
    next: Optional[RsScene] = None

    def __init__(self, name: str):
        ...

    def __repr__(self) -> str:
        ...

    def add_layer(self, caption: str) -> RsLayer:
        Temp = RsLayer(caption)
        self.layer_stack.append(Temp)
        self.trees[caption] = Temp
        return Temp

    def layer_find(self, caption: str) -> Optional[RsLayer]:
        return self.trees[caption]

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
