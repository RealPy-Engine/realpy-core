from typing import Type, Optional, List, Dict

from pygame.surface import Surface as PySurface

from ..scene import RsScene
from ..behavior import RsPrefab
from ..sprite import RsSprite

__all__ = [
    "game_speed", "dimension", "application_surface",
    "room", "room_last", "RoomOrder", "RoomPot",
    "key_map", "MouseEvents", "KeyEvents", "ControllerEvents", "OtherEvents", "RsInteruptError", 

    "Atlas", "PrefabsPot", "PrefabsPot", "AudioPot",
    "debug_set", "debug_get"
]

# General
game_speed: int = 30
_realpy_debug: bool = False


def debug_set(flag: bool):
    global _realpy_debug
    _realpy_debug = flag


def debug_get() -> bool:
    global _realpy_debug
    return _realpy_debug


# Display
dimension = (640, 480)

# Application surface
application_surface: Optional[PySurface] = None

# Rooms
room: Optional[RsScene] = None
room_last: Optional[RsScene] = None
RoomOrder: List[RsScene] = []
RoomPot: Dict[str, RsScene] = {}

# Events
key_map: Dict[int, object] = {}
MouseEvents = {}
KeyEvents = {}
ControllerEvents = {}
OtherEvents = []

class RsInteruptError(Exception):
    pass


# Sprite texture group
Atlas: Dict[str, RsSprite] = {}

# All game objects
PrefabsPot: List[Type[RsPrefab]] = []

# All sounds
AudioPot: Dict[str, object] = {}
