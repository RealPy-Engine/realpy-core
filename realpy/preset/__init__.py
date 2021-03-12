from pygame import Color

from typing import Optional

from pygame.event import Event
from pygame.surface import Surface as PySurface
from pygame import Color

from ..scene import RsScene
from ..prefab import RsPrefab
from ..sprite import RsSprite


# Display
Resolutions: tuple[int, int] = (640, 480)

# Application surface
application_surface: Optional[PySurface] = None

# Rooms
RsRoom: Optional[RsScene] = None
RsLastRoom: Optional[RsScene] = None
RoomOrder: list[RsScene] = []
RoomPot: dict[str, RsScene] = {}

# Events
Events: list[Event] = []

# Sprite texture group
Atlas: dict[str, RsSprite] = {}

# All game objects
PrefabsPot: list[type[RsPrefab]] = []

# All sounds
AudioPot: dict[str, object] = {}

# 10 px == 1 metre
phy_mess: float = 10.0 / 1
phy_velocity: float = (((1000.0 / 60.0) / 60.0) * phy_mess)

# Colors
# 1
c_white = Color(255, 255, 255)
c_ltgray = Color(192, 192, 192)
c_gray = Color(128, 128, 128)
c_dkgray = Color(64, 64, 64)
c_black = Color(0, 0, 0)

# 2
c_red = Color(255, 0, 0)
c_lime = Color(0, 255, 0)
c_green = Color(0, 128, 0)
c_blue = Color(0, 0, 255)

# 3
c_maroon = Color(128, 0, 0)
c_dkrose = Color(64, 0, 0)
c_dkgreen = Color(0, 64, 0)
c_ultramarine = Color(0, 0, 128)
c_navy = Color(0, 0, 96)

# 4
c_yellow = Color(255, 255, 0)
c_fuchsia = Color(255, 0, 255)
c_aqua = Color(0, 255, 255)

# 5
c_orange = Color(255, 128, 0)
c_cyan = Color(0, 128, 255)
c_magenta = Color(255, 0, 128)
c_purple = Color(128, 0, 255)
c_teal = Color(0, 255, 128)


class MASKS:
    RECTANGLE: int = 0
    CIRCLE: int = 2
