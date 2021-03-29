from .core import RsScene, RsLayer


class RsStage(RsScene):
    def __init__(self, name: str = ""):
        super().__init__(name)

        self.width = 640
        self.height = 480

