from typing import Type, Optional, List


class RsPrefab(object):
    """`RsPrefab`
        ---
        A template class of game object. Contains its own sprite and hierachies.

        Do not instantiate this primitive prefab.
    """

    sprite_index = None
    __parent = None
    children: List[Type] = []
    use_collision: bool = True

    def __repr__(self) -> str:
        SpriteCheck = f" ({self.sprite_index})" if self.sprite_index else ""
        return f"Prefab" + SpriteCheck + f" of {type(self)}"

    @property
    @classmethod
    def parent(cls):
        return cls.__parent

    @parent.setter
    @classmethod
    def parent(cls, target: Optional[Type]):
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
    def onAwake(itself) -> None:
        """`onAwake(instance)`
            ---
            This will run on its instance. You may override it.
        """
        pass

    @staticmethod
    def onDestroy(itself) -> None:
        """`onDestroy(instance)`
            ---
            This will run on its instance. You may override it.
        """
        pass

    @staticmethod
    def onUpdate(itself, time: float):
        """`onUpdate(instance, time)`
            ---
            This will run on its instance. You may override it.
        """
        pass

    @staticmethod
    def onUpdateLater(itself, time: float) -> None:
        """`onUpdateLater(instance, time)`
            ---
            This will run on its instance. You may override it.
        """
        pass

    @staticmethod
    def onDraw(itself, time: float) -> None:
        """`onAwake(instance, time)`
            ---
            This will run on its instance. You may override it.
        """

        itself.draw_self()
