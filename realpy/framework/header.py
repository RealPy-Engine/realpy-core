import asyncio
import sys

import pygame
import pygame.constants as PyConstants
import pygame.display as PyDisplay
import pygame.fastevent as PyEvent
from pygame.time import Clock

__all__ = ["rs_init", "rs_startup", "rs_quit"]

mouse_igniter = []
key_igniter = []
controller_igniter = []
mouse_proceed = []
key_proceed = []
controller_proceed = []
other_proceed = []


async def proceed_ing(where, pack):
    from realpy.constants import INPUT_STATES

    while True:
        try:
            Upk = where.pop()
            if pack.get(Upk) == INPUT_STATES.RELEASED:
                pack[Upk] = INPUT_STATES.NONE
                break
            pack[Upk] = INPUT_STATES.ING
            print("Start at later:", Upk)
        except IndexError:
            break
    where.clear()


async def proceed_done(where, pack):
    from realpy.constants import INPUT_STATES

    while True:
        try:
            Upk = where.pop()
            pack[Upk] = INPUT_STATES.NONE
            print("Cleaned at later:", Upk)
        except IndexError:
            break
    where.clear()


async def hand_update():
    from realpy.constants import INPUT_STATES
    from realpy.preset import RsPreset

    RsPreset.OtherEvents.clear()

    # Await
    Temp = PyEvent.get()
    Len = len(Temp)

    await asyncio.gather(proceed_ing(mouse_igniter, RsPreset.MouseEvents),
    proceed_ing(key_igniter, RsPreset.KeyEvents),
    proceed_ing(controller_igniter, RsPreset.ControllerEvents),
    proceed_done(mouse_proceed, RsPreset.MouseEvents),
    proceed_done(key_proceed, RsPreset.KeyEvents),
    proceed_done(controller_proceed, RsPreset.ControllerEvents))

    if 0 < Len:
        for event in Temp:
            if event.type == PyConstants.QUIT:
                raise RsPreset.RsInteruptError

            elif event.type == PyConstants.KEYDOWN:
                Seed: int = event.key
                Place = RsPreset.KeyEvents.get(Seed)

                if Place:  # Key can be able to be None
                    if Place == INPUT_STATES.NONE:
                        RsPreset.KeyEvents[Seed] = INPUT_STATES.PRESSED
                        print("Pressed:", Seed)
                    elif Place == INPUT_STATES.RELEASED:
                        RsPreset.KeyEvents[Seed] = INPUT_STATES.NONE
                        print("Cleaned in Press:", Seed)
                    else:
                        RsPreset.KeyEvents[Seed] = INPUT_STATES.ING
                        print("Pressing:", Seed)
                else:  # Add a new key
                    key_igniter.append(Seed)
                    RsPreset.KeyEvents[Seed] = INPUT_STATES.PRESSED
                    print("New Press:", Seed)

            elif event.type == PyConstants.KEYUP:
                Seed = event.key
                Place = RsPreset.KeyEvents.get(Seed)

                if Place:
                    if Place == INPUT_STATES.RELEASED:
                        RsPreset.KeyEvents[Seed] = INPUT_STATES.NONE
                        print("Cleaned:", Seed)
                    elif Place != INPUT_STATES.NONE:
                        key_proceed.append(Seed)  # clear later
                        RsPreset.KeyEvents[Seed] = INPUT_STATES.RELEASED
                        print("Released:", Seed)
                else:
                    RsPreset.KeyEvents[Seed] = INPUT_STATES.NONE

            elif event.type == PyConstants.MOUSEBUTTONDOWN:
                Seed: int = event.button
                Place = RsPreset.MouseEvents.get(Seed)
                RsPreset.mouse_x, RsPreset.mouse_y = event.pos

                if Place:  # Key can be able to be None
                    if Place == INPUT_STATES.NONE:
                        RsPreset.MouseEvents[Seed] = INPUT_STATES.PRESSED
                        print("Clicked:", Seed)
                    elif Place == INPUT_STATES.RELEASED:
                        RsPreset.MouseEvents[Seed] = INPUT_STATES.NONE
                        print("Cleaned in Click:", Seed)
                    else:
                        RsPreset.MouseEvents[Seed] = INPUT_STATES.ING
                        print("Clicking:", Seed)
                else:
                    mouse_igniter.append(Seed)
                    RsPreset.MouseEvents[Seed] = INPUT_STATES.PRESSED
                    print("New Click:", Seed)

            elif event.type == PyConstants.MOUSEBUTTONUP:
                Seed = event.button
                Place = RsPreset.MouseEvents.get(Seed)
                RsPreset.mouse_x, RsPreset.mouse_y = event.pos

                if Place:
                    if Place == INPUT_STATES.RELEASED:
                        RsPreset.MouseEvents[Seed] = INPUT_STATES.NONE
                        print("Cleaned:", Seed)
                    elif Place != INPUT_STATES.NONE:
                        mouse_proceed.append(Seed)  # clear later
                        RsPreset.MouseEvents[Seed] = INPUT_STATES.RELEASED
                        print("Declicked:", Seed)
                else:
                    RsPreset.MouseEvents[Seed] = INPUT_STATES.NONE

            elif event.type == PyConstants.MOUSEMOTION:
                RsPreset.mouse_x, RsPreset.mouse_y = event.pos
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
    await asyncio.gather(scene_update(room, time), graphics_update(room, time))


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
    Rooms = RsPreset.room_order
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
            asyncio.run(hand_update())
            asyncio.run(update_all(RoomCurrent, TimeOccured))
        except RsPreset.RsInteruptError:
            rs_quit()

        AbsoluteTimer.tick(RsPreset.game_speed)
        RoomCurrent = RsPreset.room


def rs_quit():
    print("Program is ended.")
    pygame.quit()
    sys.exit(0)
