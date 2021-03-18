from copy import copy
from typing import Optional

from numpy.matrixlib import mat, bmat

from ..sprite import RsSprite
from ..utility import lengthdir_x, lengthdir_y, point_distance, point_direction


class RsInstance(object):
    """`RsInstance(Prefab, Scene, Layer, x, y)`
        ---
        Derived from prefabs.
    """

    def __init__(self, original, scene, layer, x: float = 0, y: float = 0):
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
        self.friction: float = 0
        if self.__sprite_index:
            self.boundbox = copy(self.__sprite_index.boundbox)
            self.bound_vertexes = copy(self.__sprite_index.boundbox)
        else:
            self.boundbox = None
            self.bound_vertexes = None

    @property
    def sprite_index(self) -> Optional[RsSprite]:
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
    def sprite_index(self, index: Optional[RsSprite]):
        # Update the original boundbox
        if not index: # Free the memory
            self.__sprite_index = None
            del self.boundbox
            del self.bound_vertexes
        elif not self.__sprite_index: # Create boundbox
            self.__sprite_index = index
            self.boundbox = copy(index.boundbox)
            self.bound_vertexes = copy(index.boundbox)
            if self.__image_angle != 0: # Rotate
                self._set_vertex_boundary(self.__image_angle)
        else: # Don't update the currrent boundbox
            self.__sprite_index = index

    @image_angle.setter
    def image_angle(self, value: float):
        # Update the actual boundbox
        if self.__image_angle != value:
            self.__image_angle = value
            if self.__sprite_index:
                self._set_vertex_boundary(value)

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

        if self.friction != 0:
            if 0 < self.speed:
                self.speed = max(0, self.speed - self.friction)
            elif self.speed < 0:
                self.speed = min(0, self.speed + self.friction)

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

    def draw_self(self) -> bool:
        from ..preset import RsPreset

        if self.sprite_index:
            self.sprite_index.draw(RsPreset.application_surface, self.image_index, self.x, self.y, self.image_scale, self.image_angle, self.image_alpha)
            from pygame import draw

            where = RsPreset.application_surface
            draw.line(where, "red", self.bound_vertexes[0], self.bound_vertexes[1])
            draw.line(where, "red", self.bound_vertexes[1], self.bound_vertexes[3])
            draw.line(where, "red", self.bound_vertexes[3], self.bound_vertexes[2])
            draw.line(where, "red", self.bound_vertexes[2], self.bound_vertexes[0])
            draw.circle(where, "red", (self.x, self.y), 8)
            return True
        else:
            return False

    def _set_vertex_boundary(self, angle: float) -> None:
        Cos = lengthdir_x(self.image_scale, angle)
        Sin = lengthdir_y(self.image_scale, angle)
        # XOffCos = lengthdir_x(self.__sprite_index.xoffset, angle)
        # YOffCos = lengthdir_y(self.__sprite_index.yoffset, angle)

        TempTransitioner = (self.x, self.y)
        TempRotator = mat([[Cos, Sin], [-Sin, Cos]])
        for i in range(0, 4):
            TempPoint = ((self.boundbox[i] * TempRotator).tolist())[0]
            TempA = round(self.x + TempPoint[0])
            TempB = round(self.y + TempPoint[1])
            # print("Point(", i, ") - ", TempPoint, " -> (", TempA, ", ", TempB, ")")

            self.bound_vertexes[i] = (TempA, TempB)
