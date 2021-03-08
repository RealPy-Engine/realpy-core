from typing import Optional

from RsCore.prefab import RsPrefab
from RsCore.utility import *


class RsObject(object):
    link_original: Optional[RsPrefab]
    def __init__(self, scene, layer, x=0, y=0):
        self.link_original = None
        self.__enabled = True
        self.__visible = True
        self.scene = scene
        self.layer = layer
        self.x = x
        self.y = y

    @property
    def enabled(self):
        return self.__enabled

    @property
    def visible(self):
        return self.__visible

    @enabled.setter
    def enabled(self, flag):
        self.__enabled = flag

    @visible.setter
    def visible(self, flag):
        self.__visible = flag

    def onAwake(self):
        if self.link_original:
            self.link_original.onAwake(self)

    def onDestroy(self):
        if self.link_original:
            self.link_original.onDestroy(self)

    def onUpdate(self, time):
        if self.link_original:
            self.link_original.onUpdate(time, self)

    def onUpdateLater(self, time):
        if self.link_original:
            self.link_original.onUpdateLater(time, self)

    def onDraw(self, time):
        if self.link_original:
            self.link_original.onDraw(time, self)

    def onGUI(self, time):
        if self.link_original:
            self.link_original.onGUI(time, self)


class RsDirtyObject(RsObject):
    def __init__(self, scene, layer, x=0, y=0):
        super().__init__(scene, layer, x, y)

        self.image_angle = 0
        self.image_index = 0
        self.__speed = 0
        self.__direction = 0
        self.__hspeed = 0
        self.__vspeed = 0
        self.gravity = {
            "force": 0,
            "direction": 0
        }

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
    def speed(self, value):
        self.__speed = value
        self.__hspeed = lengthdir_x(value, self.__direction)
        self.__vspeed = lengthdir_y(value, self.__direction)

    @direction.setter
    def direction(self, value):
        self.__direction = value
        self.__hspeed = lengthdir_x(self.__speed, self.__direction)
        self.__vspeed = lengthdir_y(self.__speed, self.__direction)

    @hspeed.setter
    def hspeed(self, value):
        self.__hspeed = value
        self.__speed = point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = point_direction(0, 0, self.__hspeed, self.__vspeed)

    @vspeed.setter
    def vspeed(self, value):
        self.__vspeed = value
        self.__speed = point_distance(0, 0, self.__hspeed, self.__vspeed)
        self.__direction = point_direction(0, 0, self.__hspeed, self.__vspeed)

    def onUpdateLater(self, time):
        super().onUpdateLater(time)

        Hspeed = self.__hspeed
        if Hspeed != 0:
            self.x += Hspeed

        Vspeed = self.__vspeed
        if Vspeed != 0:
            self.y += Vspeed
