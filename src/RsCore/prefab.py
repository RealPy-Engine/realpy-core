class RsPrefab(object):
    def __init__(self, name: str):
        self.name = name
        self.__parent = None
        self.children = []
        self.sprite_index = None
        self.serial: int = 0

    def __hash__(self) -> int:
        return self.name.__hash__()

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, target):
        if not target:
            self.__parent = None
        else:
            Parent = self.__parent
            if Parent:
                Parent.children.remove(self)
            self.__parent = target
            target.children.append(self)

    def onAwake(self, target):
        pass

    def onDestroy(self, target):
        pass

    def onUpdate(self, time, target):
        pass

    def onUpdateLater(self, time, target):
        pass

    def onDraw(self, time, target):
        pass

    def onGUI(self, time, target):
        pass
