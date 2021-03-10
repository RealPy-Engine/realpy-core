from realpy.utility import *


class RsPrefab(object):
    __parent = None
    __children = []
    __sprite_index = None
    __is_dirty = False

    def __new__(cls):
        cls.__is_dirty = False

    def __str__(self):
        return str(type(self))

    def __repr__(self):
        SpriteCheck = f" ({self.__sprite_index})" if self.__sprite_index else ""
        return f"Prefab" + SpriteCheck + f" of {(type(self)).__base__}"

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
        if cls.__is_dirty:
            Result = cls.make_instance_complex(scene, layer, x, y)
        else:
            Result = cls.make_instance(scene, layer, x, y)
        return Result

    @classmethod
    def make_instance(cls, scene, layer, x=0, y=0):
        Result = RsInstance(cls, scene, layer, x, y)
        return Result

    @classmethod
    def make_instance_complex(cls, scene, layer, x=0, y=0):
        Result = RsDirtyInstance(cls, scene, layer, x, y)
        return Result


class RsInstance(object):
    def __init__(self, original, scene, layer, x=0, y=0):
        self.enabled = True
        self.visible = True
        self.original: type[RsPrefab] = original
        self.scene = scene
        self.layer = layer
        self.x = x
        self.y = y
        layer.storage.append(self)

    def __str__(self):
        return f"Realpy Instance of {str(self.original)}"

    def __repr__(self):
        return f"Instance %s at Layer {self.layer} of the Scene {self.scene}" % id(self)
 
    def onAwake(self):
        if self.original:
            self.original.onAwake(self)

    def onDestroy(self):
        if self.original:
            self.original.onDestroy(self)

    def onUpdate(self, time):
        if self.original:
            self.original.onUpdate(self, time)

    def onUpdateLater(self, time):
        if self.original:
            self.original.onUpdateLater(self, time)

    def onDraw(self, time):
        if self.original:
            self.original.onDraw(self, time)

    def onGUI(self, time):
        if self.original:
            self.original.onGUI(self, time)


class RsDirtyInstance(RsInstance):
    def __init__(self, original, scene, layer, x=0, y=0):
        super().__init__(original, scene, layer, x, y)

        self.sprite_index = original.sprite_index
        self.image_angle = 0
        self.image_index = 0
        self.__speed = 0
        self.__direction = 0
        self.__hspeed = 0
        self.__vspeed = 0
        self.gravity_force = 0
        self.gravity_direction = 0

    @property
    def speed(self):
        return self.__speed

    @property
    def direction(self):
        return self.__direction

    @property
    def hspeed(self):
        return self.__hspeed

    @property
    def vspeed(self):
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

        if self.gravity_force != 0:
            self.__hspeed += lengthdir_x(self.gravity_force, self.gravity_direction)
            self.__vspeed += lengthdir_y(self.gravity_force, self.gravity_direction)
        
        Hspeed = self.__hspeed * time
        if Hspeed != 0:
            self.x += Hspeed

        Vspeed = self.__vspeed * time
        if Vspeed != 0:
            self.y += Vspeed
