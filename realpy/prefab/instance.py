from typing import Optional, Union

from realpy.utility import lengthdir_x, lengthdir_y, point_distance, point_direction


class RsInstance(object):
    """ RsInstance(Prefab, Scene, Layer, x=0, y=0)

        Derived from prefabs.
    """

    def __init__(self, original, scene, layer, x: float=0, y: float=0):
        self.enabled: bool = True
        self.visible: bool = True
        self.original = original
        self.scene = scene
        self.layer = layer
        self.x: float = x
        self.y: float = y
        self.sprite_index = original.sprite_index
        self.image_angle: float = 0
        self.image_index: float = 0
        self.__speed: float = 0
        self.__direction: float = 0
        self.__hspeed: float = 0
        self.__vspeed: float = 0
        self.gravity_force: float = 0
        self.gravity_direction: float = 0

        layer.storage.append(self)

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

    def onAwake(self):
        self.original.onAwake(self)

    def onDestroy(self):
        self.original.onDestroy(self)

    def onUpdate(self, time: int):
        self.original.onUpdate(self, time)

    def onUpdateLater(self, time: int):
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

    def onDraw(self, time: int):
        self.original.onDraw(self, time)

    def onGUI(self, time: int):
        self.original.onGUI(self, time)

    def __str__(self):
        return f"Realpy Instance of {str(self.original)}"

    def __repr__(self):
        return f"Instance %s at '{self.layer}' in '{self.scene}'" % id(self)