import asyncio
import sys

import pygame
import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.event as PyEvent
from pygame.time import Clock as Clock

from realpy import preset


async def scene_update(room, time):
    room.onUpdate(time)
    room.onUpdateLater(time)
    room.onDraw(time)
    room.onGUI(time)


async def event_collect():
    # TODO: summary events in a list for each types.
    preset.Events = PyEvent.get()
    for event in preset.Events:
        if event.type == PyConstants.QUIT:
            rs_quit()
        elif event.type == PyConstants.KEYDOWN and event.key == PyConstants.K_ESCAPE:
            rs_quit()
        elif event.type == PyConstants.MOUSEBUTTONDOWN:
            pass  # room_goto_next()
        elif event.type == PyConstants.MOUSEBUTTONUP:
            pass

    return len(preset.Events)


def rs_init(title: str, view_port_width: int, view_port_height: int):
    pygame.init()
    PyDisplay.init()
    PyDisplay.set_caption(title)
    PyDisplay.set_allow_screensaver(False)

    preset.Resolutions = (view_port_width, view_port_height)
    preset.RsScreen = PyDisplay.set_mode(preset.Resolutions)


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

    absolute_timer = Clock()

    # Load rooms
    print(preset.RsRoom)
    preset.RsRoom.onAwake()
    while True:
        frame_time: int = 0 if preset.RsRoom.paused else absolute_timer.get_time()
        preset.RsScreen.fill(preset.c_black)

        asyncio.run(event_collect())
        asyncio.run(scene_update(preset.RsRoom, frame_time))

        PyDisplay.flip()
        absolute_timer.tick()


def rs_quit():
    print("Program is ended.")
    pygame.quit()
    sys.exit()