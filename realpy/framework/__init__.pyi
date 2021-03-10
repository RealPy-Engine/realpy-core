import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.event as PyEvent
from pygame.surface import Surface as PySurface
from pygame.time import Clock as Clock

from realpy.scene import RsScene

__all__ = [
    "rs_init", "rs_startup", "rs_quit"
]


async def scene_update(room: RsScene, time: int):
    ...


async def event_collect() -> int:
    ...


def rs_init(title: str, view_port_width: int, view_port_height: int):
    ...


def rs_startup():
    ...


def rs_quit():
    ...
