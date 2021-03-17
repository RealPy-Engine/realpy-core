from typing import Optional
from numpy.matrixlib import mat, bmat

from ..utility import lengthdir_x, lengthdir_y, point_distance, point_direction


class RsInstance(object):
    """`RsInstance(Prefab, Scene, Layer, x, y)`
        ---
        Derived from prefabs.
    """

    def __init__(self, original, scene, layer, x: float = 0, y: float = 0):
        from ..sprite import RsSprite

        self.enabled: bool = True
        self.visible: bool = True
        self.original = original
        self.scene = scene
        self.layer = layer
        self.x: float = x
        self.y: float = y
        self.__sprite_index: Optional[RsSprite] = original.sprite_index
        self.image_index: float = 0
        self.__image_angle: float = 0
        self.image_scale: float = 1
        self.image_alpha: float = 1
        self.__speed: float = 0
        self.__direction: float = 0
        self.__hspeed: float = 0
        self.__vspeed: float = 0
        self.gravity_force: float = 0
        self.gravity_direction: float = 0
        if self.sprite_index:
            sx, sw = self.sprite_index.xoffset, self.sprite_index.width
            sy, sh = self.sprite_index.yoffset, self.sprite_index.height
            self.boundbox = [[-sx, sw - sx], [-sy, sh - sy]]
            self.bound_vertexes = mat([-sx, sw - sx], [-sy, sh - sy])
        else:
            self.boundbox = None
            self.bound_vertexes = None

    @property
    def sprite_index(self):
        return self.__sprite_index

    @property
    def speed(self) -> float:
        return self.__speed

    @property
    def direction(self) -> float:
        return self.__direction

    @property
    def hspeed(self) -> float:
        return self.__hspeed

    @property
    def vspeed(self) -> float:
        return self.__vspeed

    @property
    def image_angle(self) -> float:
        return self.__image_angle

    @speed.setter
    def speed(self, value: float):
        self.__speed = value
        self.__hspeed = lengthdir_x(value, self.__direction)
        self.__vspeed = lengthdir_y(value, self.__direction)

    @direction.setter
    def direction(self, value: float):
        self.__direction = value
        self.__hspeed = lengthdir_x(self.__speed, self.__direction)
        self.__vspeed = lengthdir_y(self.__speed, self.__direction)

    @hspeed.setter
    def hspeed(self, value: float):
        self.__hspeed = value
        self.__speed = point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = point_direction(0, 0, self.__hspeed, self.__vspeed)

    @vspeed.setter
    def vspeed(self, value: float):
        self.__vspeed = value
        self.__speed = point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = point_direction(0, 0, self.__hspeed, self.__vspeed)

    @sprite_index.setter
    def sprite_index(self, index):
        # Update the original boundbox
        if not index: # Free the memory
            self.__sprite_index = None
            del self.boundbox
            del self.bound_vertexes
        elif not self.__sprite_index: # Create boundbox
            self.__sprite_index = index
            sx, sw = self.__sprite_index.xoffset, self.__sprite_index.width
            sy, sh = self.__sprite_index.yoffset, self.__sprite_index.height
            self.boundbox = mat([[-sx, sw - sx], [-sy, sh - sy]])
            self.bound_vertexes = mat([-sx, sw - sx], [-sy, sh - sy])
            if self.__image_angle != 0: # Rotate
                Cos = lengthdir_x(self.image_scale, self.__image_angle)
                Sin = lengthdir_y(self.image_scale, self.__image_angle)
                self.bound_vertexes = self.boundbox * mat([Cos, Sin], [-Sin, Cos])
        else: # Don't update the currrent boundbox
            self.__sprite_index = index

    @image_angle.setter
    def image_angle(self, value: float):
        # Update the actual boundbox
        if self.__image_angle != value:
            self.__image_angle = value
            if self.__sprite_index:
                Cos = lengthdir_x(self.image_scale, value)
                Sin = lengthdir_y(self.image_scale, value)
                self.bound_vertexes = self.boundbox * mat([Cos, -Sin], [Sin, Cos])

    def onAwake(self) -> None:
        """`onAwake()`
            ---
            Do not override it.
        """
        self.original.onAwake(self)

    def onDestroy(self) -> None:
        """`onDestroy()`
            ---
            Do not override it.
        """
        self.original.onDestroy(self)

    def onUpdate(self, time: float) -> None:
        """`onUpdate(time)`
            ---
            Do not override it.
        """
        self.original.onUpdate(self, time)

    def onUpdateLater(self, time: float) -> None:
        """`onUpdateLater(time)`
            ---
            Do not override it.
        """
        self.original.onUpdateLater(self, time)

        if self.gravity_force != 0:
            self.__hspeed += lengthdir_x(self.gravity_force, self.gravity_direction)
            self.__vspeed += lengthdir_y(self.gravity_force, self.gravity_direction)

        Hspeed = self.__hspeed * time
        if Hspeed != 0:
            self.x += Hspeed

        Vspeed = self.__vspeed * time
        if Vspeed != 0:
            self.y += Vspeed

    def onDraw(self, time: float) -> None:
        """`onDraw(time)`
            ---
            Do not override it.
        """
        self.original.onDraw(self, time)

    def __str__(self) -> str:
        return f"Realpy Instance of {str(self.original)}"

    def __repr__(self) -> str:
        return f"Instance %s at '{self.layer}' in '{self.scene}'" % id(self)
