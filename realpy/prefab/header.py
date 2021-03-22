from .instance import RsInstance


class RsPrefab(object):
    """`RsPrefab`
        ---
        Predefined behavior object.

        Do not instantiate it.
    """

    name: str = ""
    sprite_index = None
    use_collision: bool = True
    trait_instance = RsInstance

    def __repr__(self) -> str:
        SpriteCheck = f" ({self.sprite_index})" if self.sprite_index else ""
        return f"Prefab" + SpriteCheck + f" of {type(self)}"

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
