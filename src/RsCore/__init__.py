import asyncio
import sys

import pygame
import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.event as PyEvent
from pygame.time import Clock as Clock

from RsCore import constants as RsConstants, containers as RsContainers


async def scene_update(room, time):
    room.onUpdate(time)
    room.onUpdateLater(time)
    room.onDraw(time)
    room.onGUI(time)


async def event_collect():
    # TODO: summary events in a list for each types.
    RsContainers.Events = PyEvent.get()
    for event in RsContainers.Events:
        if event.type == PyConstants.QUIT:
            rs_quit()
        elif event.type == PyConstants.KEYDOWN and event.key == PyConstants.K_ESCAPE:
            rs_quit()
        elif event.type == PyConstants.MOUSEBUTTONDOWN:
            pass  # room_goto_next()
        elif event.type == PyConstants.MOUSEBUTTONUP:
            pass

    return len(RsContainers.Events)


def init(title: str, view_port_width: int, view_port_height: int):
    pygame.init()
    PyDisplay.init()
    PyDisplay.set_caption(title)
    PyDisplay.set_allow_screensaver(False)

    RsConstants.Resolutions = (view_port_width, view_port_height)
    RsContainers.RsScreen = PyDisplay.set_mode(RsConstants.Resolutions)


def startup():
    # Startup
    Rooms = RsContainers.RoomOrder
    Temp = Rooms[0]

    if not Temp:
        raise RuntimeError("No scene found.")
    RsContainers.RsRoom = Temp

    absolute_timer = Clock()

    # Load rooms
    print(RsContainers.RsRoom)
    RsContainers.RsRoom.onAwake()
    while True:
        frame_time: int = 0 if RsContainers.RsRoom.paused else absolute_timer.get_time()
        RsContainers.RsScreen.fill(RsConstants.c_black)

        asyncio.run(event_collect())
        asyncio.run(scene_update(RsContainers.RsRoom, frame_time))

        PyDisplay.flip()
        absolute_timer.tick()


def rs_quit():
    rs_cleanup()
    sys.exit()


def rs_cleanup():
    print("Program is ended.")
    pygame.quit()
