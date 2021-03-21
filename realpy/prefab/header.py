from typing import Type

from .backend import RsGameObject
from .instance import RsInstance


class RsPrefab(object):
    """`RsPrefab`
        ---
        Predefined behavior object.
    """

    trait_api = RsGameObject
    trait_instance = RsInstance

    def onAwake(self):
        """`onAwake(instance)`
            ---
            This will run on its instance. You may override it.
        """
        return self.trait_api.onAwake

    def onDestroy(self) -> None:
        """`onDestroy(instance)`
            ---
            This will run on its instance. You may override it.
        """
        pass

    def onUpdate(self, time: float):
        """`onUpdate(instance, time)`
            ---
            This will run on its instance. You may override it.
        """
        pass

    def onUpdateLater(self, time: float) -> None:
        """`onUpdateLater(instance, time)`
            ---
            This will run on its instance. You may override it.
        """
        pass

