from typing import Any, Optional


class RsScene(object):
    """`RsScene(name)`
        ---
        Large portion of game pipeline.
    """
    def __init__(self, name: str=""):
        self.name: str = name
        self.layer_stack: list = []
        self.trees: dict[str, Any] = {}
        self.paused: bool = False
        self.EveryInstancesPot: list = []
        self.SpecificInstancesPot: dict[int, list] = {}
        self.before: Optional[RsScene] = None
        self.next: Optional[RsScene] = None

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Realpy Scene {self.name} ({len(self.layer_stack)})"

    def add_layer_direct(self, layer):
        self.layer_stack.append(layer)
        self.trees[layer.name] = layer
        return layer

    def layer_find(self, caption: str):
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

    def onUpdate(self, time: float):
        for Layer in self.layer_stack:
            Layer.onUpdate(time)

    def onUpdateLater(self, time: float):
        for Layer in self.layer_stack:
            Layer.onUpdateLater(time)

    def onDraw(self, time: float):
        for Layer in self.layer_stack:
            Layer.onDraw(time)