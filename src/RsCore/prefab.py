from RsCore.utility import *


class RsPrefab(object):
    __parent = None
    __children = []
    __sprite_index = None

    @property
    @classmethod
    def parent(cls):
        return cls.__parent

    @parent.setter
    @classmethod
    def parent(cls, target):
        if not target:
            if cls.__parent:
                cls.__parent.children.remove(cls)
            cls.__parent = None
        else:
            Parent = cls.__parent
            if Parent:
                Parent.children.remove(cls)
            cls.__parent = target
            target.children.append(cls)

    @property
    @classmethod
    def children(cls):
        return cls.__children

    @property
    @classmethod
    def sprite_index(cls):
        return cls.__sprite_index

    @staticmethod
    def onAwake(target):
        pass

    @staticmethod
    def onDestroy(target):
        pass

    @staticmethod
    def onUpdate(target, time):
        pass

    @staticmethod
    def onUpdateLater(target, time):
        pass

    @staticmethod
    def onDraw(target, time):
        pass

    @staticmethod
    def onGUI(target, time):
        pass

    @classmethod
    def instantiate(cls, scene, layer, x=0, y=0):
        Result = RsInstance(cls, scene, layer, x, y)
        return Result

    @classmethod
    def instantiate_complex(cls, scene, layer, x=0, y=0):
        Result = RsDirtyInstance(cls, scene, layer, x, y)
        return Result


class RsInstance(object):
    def __init__(self, original, scene, layer, x=0, y=0):
        self.enabled = True
        self.visible = True
        self.original = original
        self.scene = scene
        self.layer = layer
        self.x = x
        self.y = y

    def onAwake(self):
        if self.original:
            self.original.onAwake(self)

    def onDestroy(self):
        if self.original:
            self.original.onDestroy(self)

    def onUpdate(self):
        if self.original:
            self.original.onUpdate(self)

    def onUpdateLater(self):
        if self.original:
            self.original.onUpdateLater(self)

    def onDraw(self):
        if self.original:
            self.original.onDraw(self)

    def onGUI(self):
        if self.original:
            self.original.onGUI(self)


class RsDirtyInstance(RsInstance):
    def __init__(self, original, scene, layer, x=0, y=0):
        super().__init__(original, scene, layer, x, y)

        self.image_angle = 0
        self.image_index = 0
        self.__speed = 0
        self.__direction = 0
        self.__hspeed = 0
        self.__vspeed = 0
        self.gravity_force = 0
        self.gravity_direction = 0

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
        super().onUpdateLater()

        if self.gravity_force != 0:
            self.__hspeed += lengthdir_x(self.gravity_force, self.gravity_direction)
            self.__vspeed += lengthdir_y(self.gravity_force, self.gravity_direction)
        
        Hspeed = self.__hspeed
        if Hspeed != 0:
            self.x += Hspeed

        Vspeed = self.__vspeed
        if Vspeed != 0:
            self.y += Vspeed


