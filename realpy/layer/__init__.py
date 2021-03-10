class RsLayer(object):
    def __init__(self, name: str):
        self.name = name
        self.storage = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Layer " + str(self)

    def onAwake(self):
        for Instance in self.storage:
            Instance.onAwake()

    def onDestroy(self):
        for Instance in self.storage:
            Instance.onDestroy()

    def onUpdate(self, time):
        for Instance in self.storage:
            Instance.onUpdate(time)

    def onUpdateLater(self, time):
        for Instance in self.storage:
            Instance.onUpdateLater(time)

    def onDraw(self, time):
        for Instance in self.storage:
            Instance.onDraw(time)

    def onGUI(self, time):
        for Instance in self.storage:
            Instance.onGUI(time)
