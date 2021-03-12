from typing import Optional

from realpy.sprite import RsSprite


class RsPrefab(type):
    """ RsPrefab

        A template class of game object. Contains its own sprite and hierachies.

        Do not instantiate this primitive prefab.
    """

    def __new__(cls, *args, **kargs):
        cls.__parent: Optional[type[RsPrefab]]  = None
        cls.children: Optional[list[type[RsPrefab]]] = []
        cls.sprite_index: Optional[RsSprite] = None
        return super().__new__(cls, *args, **kargs)

    def __str__(self) -> str:
        return str(type(self))

    def __repr__(self) -> str:
        SpriteCheck = f" ({self.sprite_index})" if self.sprite_index else ""
        return f"Prefab" + SpriteCheck + f" of {type(self)}"

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

    @staticmethod
    def onAwake(itself):
        pass

    @staticmethod
    def onDestroy(itself):
        pass

    @staticmethod
    def onUpdate(itself, time: int):
        pass

    @staticmethod
    def onUpdateLater(itself, time: int):
        pass

    @staticmethod
    def onDraw(itself, time: int):
        pass

    @staticmethod
    def onGUI(itself, time: int):
        pass

    @classmethod
    def instantiate(cls, scene, layer, x: float=0, y: float=0):
        """instantiate(Scene, Layer, x=0, y=0)

            Creates a instance of game object.
        """
 
        from .instance import RsInstance

        Result = RsInstance(cls, scene, layer, x, y)
        return Result

