from typing import overload
from realpy.layer import RsLayer


class RsScene(object):
    def __init__(self, name):
        self.name = name
        self.layer_stack = []
        self.trees = {}
        self.paused = False
        self.EveryInstancesPot = []
        self.SpecificInstancesPot = {}
        self.before = None
        self.next = None

    def __str__(self):
        return f"Realpy Scene {self.name}"

    def __repr__(self):
        return f"Realpy Scene {self.name} ({len(self.layer_stack)})"

    def add_layer(self, caption):
        Temp = RsLayer(caption)
        self.layer_stack.append(Temp)
        self.trees[caption] = Temp
        return Temp

    def add_layer_direct(self, layer):
        self.layer_stack.append(layer.name)
        self.trees[layer.name] = layer
        return layer

    def layer_find(self, caption):
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

    def onUpdate(self, time):
        for Layer in self.layer_stack:
            Layer.onUpdate(time)

    def onUpdateLater(self, time):
        for Layer in self.layer_stack:
            Layer.onUpdateLater(time)

    def onDraw(self, time):
        for Layer in self.layer_stack:
            Layer.onDraw(time)

    def onGUI(self, time):
        for Layer in self.layer_stack:
            Layer.onGUI(time)
