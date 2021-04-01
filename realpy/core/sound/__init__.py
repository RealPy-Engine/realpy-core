from _typeshed import NoneType
from typing import Optional, Union, overload

from pygame import mixer as PyAudio
from pygame import music as PyMusic
from pygame.mixer import Channel as PyChannel, Sound as PySound

from .control import *
from .sfx import *
from .stream import *

audio_set_channel_count = PyAudio.set_num_channels
audio_get_channel_count = PyAudio.get_num_channels
AudioType = Optional[Union[PySound, RsSound]]


def audio_play(sound: RsSound, loop = False):
    return sound.play(-1) if loop else sound.play()


def audio_stop(sound: Optional[RsSound] = None):
    if sound:
        sound.stop()
    else:
        PyAudio.stop()


def audio_play_single(sound: RsSound, loop = False):
    sound.stop()
    audio_play(sound, loop)


def audio_pause(sound: Optional[RsSound] = None):
    if sound:
        if sound.is_playing():
            for Place in sound.fields:
                if Place.get_sound() is sound:
                    Place.pause()
    else:
        PyAudio.pause() 


def audio_resume(sound: Optional[RsSound] = None):
    if sound:
        for Place in sound.fields:
                if Place.get_sound() is sound:
                    Place.unpause()
    else:
        PyAudio.unpause()


@overload
def audio_is_playing(sound: None) -> bool:
    return PyAudio.get_busy()


@overload
def audio_is_playing(sound: PySound) -> bool:
    return 0 < sound.get_num_channels()


@overload
def audio_is_playing(sound: PyChannel) -> bool:
    return sound.get_busy()


def audio_is_playing(sound) -> bool:
    return audio_is_playing(sound)
