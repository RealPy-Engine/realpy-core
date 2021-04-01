from pygame import music as PyMusic


class RsMusic:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = PyMusic.load(filepath)
