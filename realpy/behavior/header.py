from .instance import RsInstance


class RsPrefab(object):
    """`RsPrefab`
        ---
        Predefined behavior object.

        Do not instantiate it.

        ### How to make flow methods
        - onAwake
        - onDestroy
        - onUpdate
        - onUpdateLater
        - onDraw

        ```
        @staticmethod
        def onDraw(itself, time: float) -> None:
            pass
        ```
    """

    name: str = ""
    sprite_index = None
    use_collision: bool = True
    trait_instance = RsInstance

    onAwake = None
    onDestroy = None
    onUpdate = None
    onUpdateLater = None
    onDraw = None

    @staticmethod
    def onTest(itself, time: float) -> None:
        """`onTest(instance, time)`
            ---
            This will run on its instance. You may override it.
        """
        pass
