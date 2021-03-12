from typing import Union

from realpy import preset
from realpy.scene import RsScene


def room_register(info: Union[str, RsScene]):
    NewRoom: RsScene
    Name: str
    if type(info) is str:
        NewRoom = RsScene(info)
        Name = info
    elif type(info) is RsScene:
        NewRoom = info
        Name = info.name
    else:
        raise TypeError("No specific scene found.")

    Number = len(preset.RoomOrder)
    if 0 < Number:
        LastRoom = preset.RsLastRoom
        if LastRoom and NewRoom:
            NewRoom.before = LastRoom
            LastRoom.next = NewRoom
    else:
        preset.RsRoom = NewRoom
        preset.RsLastRoom = NewRoom

    preset.RoomOrder.append(NewRoom)
    preset.RoomPot[Name] = NewRoom
    return NewRoom


def room_get(id: Union[int, str]):
    if type(id) is int:
        return preset.RoomOrder[id]
    elif type(id) is str:
        return preset.RoomPot[id]


def room_set(taget: RsScene):
    if preset.RsRoom:
        preset.RsRoom.onDestroy()
    preset.RsRoom = taget
    preset.RsRoom.onAwake()
    print("Go to " + str(preset.RsRoom))


def room_goto(name: str):
    Temp = room_get(name)
    if not Temp:
        raise RuntimeError("The room " + name + " doesn't exist.")
    elif Temp is not preset.RsRoom:
        room_set(Temp)


def room_goto_next():
    Next = preset.RsRoom.next
    if Next:
        room_set(Next)
    else:
        raise RuntimeError("The next room doesn't exist.\n")
