from typing import List, Optional

from pygame import mixer as PyAudio
from pygame.mixer import Channel as PyChannel, Sound as PySound

__all__ = ["RsSound"]


# TODO: #42 Audio System
class RsSound(PySound):
    def __init__(self, info):
        super().__init__(info)
        self.fields = []

    # def play(self, loops: Optional[int], maxtime: Optional[int], fade_ms: Optional[int]) -> Optional[PyChannel]:
        """
        Place: Optional[PyChannel] = PyAudio.find_channel(False)
        if not Place:
            return None
        else:
            Place.play(self, loops, maxtime, fade_ms)
            return Place
        """

    def is_playing(self) -> bool:
        return 0 < self.get_num_channels()
