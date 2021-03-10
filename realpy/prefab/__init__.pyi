from typing import Optional, Type

from realpy.scene import RsScene
from realpy.layer import RsLayer
from realpy.sprite import RsSprite


class RsPrefab(object):
    """
        RsPrefab()

        A preset of game object. Contains its own sprite and hierachies.
    """
    __parent: Optional[Type[RsPrefab]]
    __children: Optional[list[Type[RsPrefab]]]
    __sprite_index: Optional[RsSprite]

    @classmethod
    def __str__(cls) -> str:
        ...

    @classmethod
    def __repr__(cls) -> str:
        ...

    @property
    @classmethod
    def parent(cls) -> Optional[Type[RsPrefab]]:
        ...

    @parent.setter
    @classmethod
    def parent(cls, target: Optional[Type[RsPrefab]]):
        ...

    @property
    @classmethod
    def children(cls) -> Optional[list[Type[RsPrefab]]]:
        ...

    @staticmethod
    def onAwake(target: RsInstance):
        ...

    @staticmethod
    def onDestroy(target: RsInstance):
        ...

    @staticmethod
    def onUpdate(target: RsInstance, time: int):
        ...

    @staticmethod
    def onUpdateLater(target: RsInstance, time: int):
        ...

    @staticmethod
    def onDraw(target: RsInstance, time: int):
        ...

    @staticmethod
    def onGUI(target: RsInstance, time: int):
        ...

    @classmethod
    def instantiate(cls, scene: RsScene, layer: RsLayer, x: float=0, y: float=0) -> RsInstance:
        ...

    @classmethod
    def instantiate_complex(cls, scene: RsScene, layer: RsLayer, x: float=0, y: float=0) -> RsDirtyInstance:
        ...

    ...


class RsInstance(object):
    """
        RsInstance(Prefab, Scene, Layer, x=0, y=0)

        A derived object from prefabs.
    """
    enabled: bool
    visible: bool
    original: Type[RsPrefab]
    scene: RsScene
    layer: RsLayer
    x: float
    y: float

    def __init__(self, original: Type[RsPrefab], scene: RsScene, layer: RsLayer, x: float=0, y: float=0):
        ...

    def __str__(self) -> str:
        ...

    def __repr__(self) -> str:
        ...

    ...


class RsDirtyInstance(RsInstance):
    """
        RsDirtyInstance(Prefab, Scene, Layer, x=0, y=0)

        A derived object from prefabs. Has physical attributes.
    """
    sprite_index: Optional[RsSprite]
    image_angle: float
    image_index: float
    __speed: float
    __direction: float
    __hspeed: float
    __vspeed: float
    gravity_force: float
    gravity_direction: float

    def __init__(self, original: Type[RsPrefab], scene: RsScene, layer: RsLayer, x: float = 0, y: float = 0):
        ...

    @property
    def speed(self) -> float:
        ...

    @property
    def direction(self) -> float:
        ...

    @property
    def hspeed(self) -> float:
        ...

    @property
    def vspeed(self) -> float:
        ...

    @speed.setter
    def speed(self, value):
        ...

    @direction.setter
    def direction(self, value):
        ...

    @hspeed.setter
    def hspeed(self, value):
        ...

    @vspeed.setter
    def vspeed(self, value):
        ...

    def onUpdateLater(self, time: int):
        ...

    ...


