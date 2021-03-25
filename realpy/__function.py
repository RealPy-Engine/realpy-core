from realpy.constants import INPUT_STATES
from realpy.preset import RsPreset


# TODO: #40 input wrapper functions
def keyboard_check(key: int) -> bool:
    Place = RsPreset.KeyEvents.get(key)
    if Place and Place == INPUT_STATES.ING or Place == INPUT_STATES.PRESSED:
        return True
    else:
        return False


def keyboard_check_pressed(key: int) -> bool:
    Place = RsPreset.KeyEvents.get(key)
    if Place and Place == INPUT_STATES.PRESSED:
        return True
    else:
        return False


def keyboard_check_released(key: int) -> bool:
    Place = RsPreset.KeyEvents.get(key)
    if Place and Place == INPUT_STATES.RELEASED:
        return True
    else:
        return False


def mouse_check(button: int) -> bool:
    Place = RsPreset.MouseEvents.get(button)
    if Place and Place == INPUT_STATES.ING or Place == INPUT_STATES.PRESSED:
        return True
    else:
        return False


def mouse_check_pressed(button: int) -> bool:
    Place = RsPreset.MouseEvents.get(button)
    if Place and Place == INPUT_STATES.PRESSED:
        return True
    else:
        return False


def mouse_check_released(button: int) -> bool:
    Place = RsPreset.MouseEvents.get(button)
    if Place and Place == INPUT_STATES.RELEASED:
        return True
    else:
        return False
