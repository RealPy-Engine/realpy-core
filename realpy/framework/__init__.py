import asyncio, sys
from realpy.utility import irandom

import pygame
import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.fastevent as PyEvent
from pygame.time import Clock as Clock

from .. import preset
from ..scene import RsScene

__all__ = ("rs_init", "rs_startup", "rs_quit")


async def hand_update():
    preset.Events.clear()

    # Await
    Temp = PyEvent.get()

    for event in Temp:
        if event.type == PyConstants.QUIT:
            rs_quit()
        elif event.type == PyConstants.KEYDOWN and event.key == PyConstants.K_ESCAPE:
            rs_quit()
        elif event.type == PyConstants.MOUSEBUTTONDOWN:
            pass  # room_goto_next()
        elif event.type == PyConstants.MOUSEBUTTONUP:
            pass

    preset.Events = Temp
    return len(preset.Events)


async def scene_update(room: RsScene, time: float):
    room.onUpdate(time)
    room.onUpdateLater(time)


async def graphics_update(room: RsScene, time: float):
    preset.application_surface.fill("black")
    room.onDraw(time)
    PyDisplay.update()


async def update_all(room: RsScene, time: float):
    await asyncio.gather(hand_update(), scene_update(room, time), graphics_update(room, time))


def rs_init(title: str, view_port_width: int, view_port_height: int):
    pygame.init()
    PyDisplay.init()
    PyEvent.init()

    PyDisplay.set_caption(title)
    PyDisplay.set_allow_screensaver(False)

    preset.dimension = (view_port_width, view_port_height)
    preset.application_surface = PyDisplay.set_mode(preset.dimension)


def rs_startup():
    # Startup
    Rooms = preset.RoomOrder
    StartRoom = None
    try:
        StartRoom = Rooms[0]
        preset.RsRoom = StartRoom
    except IndexError:
        raise RuntimeError("No scene found.")

    if not StartRoom:
        raise RuntimeError("Invalid scene.")

    RoomCurrent: RsScene = preset.RsRoom
    AbsoluteTimer = Clock()
    TimeOccured: float = 0

    # Load rooms
    print(preset.RsRoom)
    preset.RsRoom.onAwake()
    while True:
        TimeOccured = 0 if preset.RsRoom.paused else AbsoluteTimer.get_time() * 0.001  # Millisecond
        print(TimeOccured)

        asyncio.run(update_all(RoomCurrent, TimeOccured))

        AbsoluteTimer.tick(preset.game_speed)
        RoomCurrent = preset.RsRoom


def rs_quit():
    print("Program is ended.")
    pygame.quit()
    sys.exit()
