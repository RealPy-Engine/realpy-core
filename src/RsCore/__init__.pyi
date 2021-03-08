from typing import Optional

import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.event as PyEvent
from pygame.surface import Surface as PySurface
from pygame.time import Clock as Clock

from .scene import RsScene
from .layer import RsLayer
from .prefab import RsPrefab
from .instance import RsObject
from .sprite import RsSprite
import RsCore.constants as RsConstants, RsCore.containers as RsContainers
from .assets import *


async def scene_update(room: RsScene, time: int):
    ...


async def event_collect() -> int:
    ...


def init(title: str, view_port_width: int, view_port_height: int):
    ...


def startup():
    ...


def rs_cleanup():
    ...


def rs_quit():
    ...
