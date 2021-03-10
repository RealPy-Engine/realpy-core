from typing import Union

from realpy import GameObject, RsDirtyInstance, RsInstance


class RsLayer(object):
    """
        RsLayer(name)

        Belongs to a scene and contains game instances.
    """
    name: str
    storage: list[GameObject]

    def __init__(self, name: str):
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
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
