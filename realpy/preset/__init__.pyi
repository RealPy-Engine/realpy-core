from typing import Optional

from pygame.event import Event
from pygame.surface import Surface as PySurface
from pygame import Color

from realpy.scene import RsScene
from realpy.prefab import RsPrefab
from realpy.sprite import RsSprite

# Display
Resolutions: tuple[int, int]

# Application surface
RsScreen: Optional[PySurface]

# Rooms
RsRoom: Optional[RsScene]
RsLastRoom: Optional[RsScene]
RoomOrder: list[RsScene]
RoomPot: dict[str, RsScene]

# Events
Events: list[Event]

# Sprite texture group
Atlas: dict[str, RsSprite]

# All game objects
PrefabsPot: list[type[RsPrefab]]

# All sounds
AudioPot: dict[str, object]

phy_mess: float
phy_velocity: float

c_white: Color
c_ltgray: Color
c_gray: Color
c_dkgray: Color
c_black: Color

c_red: Color
c_lime: Color
c_green: Color
c_blue: Color

# 3
c_maroon: Color
c_dkrose: Color
c_dkgreen: Color
c_ultramarine: Color
c_navy: Color

# 4
c_yellow: Color
c_fuchsia: Color
c_aqua: Color

# 5
c_orange: Color
c_cyan: Color
c_magenta: Color
c_purple: Color
c_teal: Color

class MASKS:
    RECTANGLE: int
    CIRCLE: int
