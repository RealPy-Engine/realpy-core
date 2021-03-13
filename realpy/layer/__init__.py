class RsLayer(object):
    """ RsLayer(name)

        Belongs to a scene and contains game instances.
    """

    def __init__(self, name: str=""):
        from realpy.prefab import RsInstance

        self.name: str = name
        self.storage: list[RsInstance] = []

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Realpy Layer {self.name} ({len(self.storage)})"

    def onAwake(self) -> None:
        for Instance in self.storage:
            Instance.onAwake()

    def onDestroy(self) -> None:
        for Instance in self.storage:
            Instance.onDestroy()

    def onUpdate(self, time: int) -> None:
        for Instance in self.storage:
            Instance.onUpdate(time)

    def onUpdateLater(self, time: int) -> None:
        for Instance in self.storage:
            Instance.onUpdateLater(time)

    def onDraw(self, time: int) -> None:
        for Instance in self.storage:
            Instance.onDraw(time)
