import asyncio
import sys

import pygame
import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.fastevent as PyEvent
from pygame.time import Clock

__all__ = ("rs_init", "rs_startup", "rs_quit")


async def hand_update():
    from realpy.preset import RsPreset

    RsPreset.MouseEvents.clear()
    RsPreset.KeyEvents.clear()
    RsPreset.ControllerEvents.clear()
    RsPreset.OtherEvents.clear()

    # Await
    Temp = PyEvent.get()
    Len = len(Temp)

    if 0 < Len:
        for event in Temp:
            if event.type == PyConstants.QUIT:
                raise RsPreset.RsInteruptError
            elif event.type in (PyConstants.KEYDOWN, PyConstants.KEYUP):
                RsPreset.KeyEvents[event.key] = event.type
            elif event.type in (PyConstants.MOUSEBUTTONDOWN, PyConstants.MOUSEBUTTONUP):
                RsPreset.MouseEvents[event.button] = (event.type, event.pos)
            elif event.type == PyConstants.MOUSEMOTION:
                RsPreset.MouseEvents[0] = (event.pos, event.rel)
            else:
                RsPreset.OtherEvents.append(event)


async def scene_update(room, time: float):
    room.onUpdate(time)
    room.onUpdateLater(time)


async def graphics_update(room, time: float):
    from realpy.preset import RsPreset

    RsPreset.application_surface.fill("black")
    room.onDraw(time)
    PyDisplay.update()


async def update_all(room, time: float):
    await asyncio.gather(hand_update(), scene_update(room, time), graphics_update(room, time))


def rs_init(title: str, view_port_width: int, view_port_height: int):
    from realpy.preset import RsPreset

    pygame.init()
    PyDisplay.init()
    PyEvent.init()

    PyDisplay.set_caption(title)
    PyDisplay.set_allow_screensaver(False)

    RsPreset.dimension = (view_port_width, view_port_height)
    RsPreset.application_surface = PyDisplay.set_mode(RsPreset.dimension)


def rs_startup():
    from realpy.preset import RsPreset
    from realpy.scene import RsScene

    # Startup
    Rooms = RsPreset.RoomOrder
    StartRoom = None
    try:
        StartRoom = Rooms[0]
        RsPreset.room = StartRoom
    except IndexError:
        raise RuntimeError("No scene found.")

    if not StartRoom:
        raise RuntimeError("Invalid scene.")

    RoomCurrent: RsScene = RsPreset.room
    AbsoluteTimer = Clock()
    TimeOccured: float = 0

    # Load rooms
    print(RsPreset.room)
    RsPreset.room.onAwake()
    while True:
        TimeOccured = 0 if RsPreset.room.paused else AbsoluteTimer.get_time() * 0.001  # Millisecond

        try:
            asyncio.run(update_all(RoomCurrent, TimeOccured), debug=RsPreset.debug_get())
        except RsPreset.RsInteruptError:
            rs_quit()

        AbsoluteTimer.tick(RsPreset.game_speed)
        RoomCurrent = RsPreset.room


def rs_quit():
    print("Program is ended.")
    pygame.quit()
    sys.exit(0)
