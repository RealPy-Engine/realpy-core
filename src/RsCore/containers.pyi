from typing import Optional

from pygame.event import Event
from pygame.surface import Surface as PySurface

from RsCore.scene import RsScene
from RsCore.prefab import RsPrefab
from RsCore.sprite import RsSprite

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
PrefabsPot: dict[str, RsPrefab]

# All sounds
AudioPot: dict[str, object]
