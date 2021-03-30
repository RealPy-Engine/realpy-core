from typing import Optional

from pygame import mixer as PySound


class RsAudio:
    def __init__(self, filepath: str):
        import os

        self.raw_data = []
        self.data: Optional[PySound.Sound] = PySound.Sound(filepath)
        self.filename = os.path.basename(filepath)

    def __str__(self) -> str:
        return self.filename
