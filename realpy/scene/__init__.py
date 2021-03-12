from typing import Optional

from realpy.layer import RsLayer


class RsScene(object):
    """ RsScene(name)

        Large portion of game pipeline.
    """

    def __init__(self, name: str):
        from realpy.prefab import RsInstance

        self.name: str = name
        self.layer_stack: list[RsLayer] = []
        self.trees: dict[str, RsLayer] = {}
        self.paused: bool = False
        self.EveryInstancesPot: list = []
        self.SpecificInstancesPot: dict[int, list[RsInstance]] = {}
        self.before: Optional[RsScene] = None
        self.next: Optional[RsScene] = None

    def __str__(self) -> str:
        return f"Realpy Scene {self.name}"

    def __repr__(self) -> str:
        return f"Realpy Scene {self.name} ({len(self.layer_stack)})"

    def add_layer_direct(self, layer: RsLayer) -> RsLayer:
        self.layer_stack.append(layer)
        self.trees[layer.name] = layer
        return layer

    def layer_find(self, caption: str) -> Optional[RsLayer]:
        return self.trees[caption]

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def onAwake(self):
        for Layer in self.layer_stack:
            Layer.onAwake()

    def onDestroy(self):
        for Layer in self.layer_stack:
            Layer.onDestroy()

    def onUpdate(self, time: int):
        for Layer in self.layer_stack:
            Layer.onUpdate(time)

    def onUpdateLater(self, time: int):
        for Layer in self.layer_stack:
            Layer.onUpdateLater(time)

    def onDraw(self, time: int):
        for Layer in self.layer_stack:
            Layer.onDraw(time)

    def onGUI(self, time: int):
        for Layer in self.layer_stack:
            Layer.onGUI(time)
