from copy import copy
from typing import List, Optional


class RsLayer(object):
    """`RsLayer(name)`
        ---
        Belongs to a scene and executes game instances.
    """

    def __init__(self, scene, name: str = ""):
        self.scene = scene
        self.name: str = name
        self.storage: List = []
        self.storage_awake: List = []
        self.storage_destroy: List = []
        self.storage_update: List = []
        self.storage_updatelater: List = []
        self.storage_draw: List = []
        self.__atomic_storage: Optional[List] = None

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return f"Realpy Layer {self.name} ({len(self.storage)})"

    def add(self, instance):
        self.storage.append(instance)
        instance.attach(self.storage)

        if instance.onAwake:
            self.storage_awake.append(instance)
            instance.attach(self.storage_awake)

        if instance.onDestroy:
            self.storage_destroy.append(instance)
            instance.attach(self.storage_destroy)

        if instance.onUpdate:
            self.storage_update.append(instance)
            instance.attach(self.storage_update)

        if instance.onUpdateLater:
            self.storage_updatelater.append(instance)
            instance.attach(self.storage_updatelater)

        if instance.onDraw:
            self.storage_draw.append(instance)
            instance.attach(self.storage_draw)

        return instance

    def onAwake(self) -> None:
        for Instance in self.storage_awake:
            Instance.onAwake()

    def onDestroy(self) -> None:
        for Instance in self.storage_destroy:
            Instance.onDestroy()

    def onUpdate(self, time: float) -> None:
        self.__atomic_storage = copy(self.storage_update)
        for Instance in self.__atomic_storage:
            Instance.onUpdate(time)

    def onUpdateLater(self, time: float) -> None:
        self.__atomic_storage = copy(self.storage_updatelater)
        for Instance in self.__atomic_storage:
            Instance.onUpdateLater(time)

    def onDraw(self, time: float) -> None:
        self.__atomic_storage = copy(self.storage_draw)
        for Instance in self.__atomic_storage:
            Instance.onDraw(time)
