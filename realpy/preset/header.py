from typing import Type, Optional, List, Dict

from pygame.event import Event
from pygame.surface import Surface as PySurface

from ..scene import RsScene
from ..prefab import RsGameObject
from ..sprite import RsSprite

__all__ = [
    "game_speed", "key_map", "dimension", "application_surface", "RsRoom", "RsLastRoom",
    "RoomOrder", "RoomPot", "Events", "Atlas", "PrefabsPot", "PrefabsPot", "AudioPot",
    "MASKS", "phy_mess", "phy_velocity", "debug_set", "debug_get"
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
application_surface: PySurface

# Rooms
RsRoom: Optional[RsScene] = None
RsLastRoom: Optional[RsScene] = None
RoomOrder: List[RsScene] = []
RoomPot: Dict[str, RsScene] = {}

# Events
key_map: Dict[int, object] = {}
Events: Dict[str, Event] = {}

# Sprite texture group
Atlas: Dict[str, RsSprite] = {}

# All game objects
PrefabsPot: List[Type[RsGameObject]] = []

# All sounds
AudioPot: Dict[str, object] = {}

# 10 px == 1 metre
phy_mess: float = 10.0 / 1
phy_velocity: float = (((1000.0 / 60.0) / 60.0) * phy_mess)


class MASKS:
    RECTANGLE: int = 0
    CIRCLE: int = 2
