from typing import Optional, Union, Type

from RsCore.scene import RsScene
from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.instance import RsObject
from RsCore import constants as RsConstants, containers as RsContainers


def object_register(name):
    Temp = RsPrefab(name)
    RsContainers.PrefabsPot[name] = Temp
    return Temp


def room_register(name):
    NewRoom = RsScene(name)

    Number = len(RsContainers.RoomOrder)
    if 0 < Number:
        LastRoom = RsContainers.RsLastRoom
        if LastRoom and NewRoom:
            NewRoom.before = LastRoom
            LastRoom.next = NewRoom
    else:
        RsContainers.RsRoom = NewRoom
        RsContainers.RsLastRoom = NewRoom

    RsContainers.RoomOrder.append(NewRoom)
    RsContainers.RoomPot[name] = NewRoom
    return NewRoom


def room_get(id):
    if type(id) is int:
        return RsContainers.RoomOrder[id]
    elif type(id) is str:
        return RsContainers.RoomPot[id]


def room_set(taget):
    if RsContainers.RsRoom:
        RsContainers.RsRoom.onDestroy()
    RsContainers.RsRoom = taget
    RsContainers.RsRoom.onAwake()
    print("Go to " + str(RsContainers.RsRoom))


def room_goto(name):
    Temp = room_get(name)
    if not Temp:
        raise RuntimeError("The room " + name + " doesn't exist.")
    elif Temp is not RsContainers.RsRoom:
        room_set(Temp)


def room_goto_next():
    Next = RsContainers.RsRoom.next
    print(Next)
    if Next:
        room_set(Next)
    else:
        raise RuntimeError("The next room doesn't exist.\n")


def global_layer_find(name):
    if RsContainers.RsRoom:
        Where = RsContainers.RsRoom.trees[name]
        return Where
    return None


def instantiate(gobject, layer, x = 0, y = 0):
    if RsContainers.RsRoom:
        Instance = gobject(RsContainers.RsRoom, layer, x, y)
        Instance.onAwake()

        RsContainers.RsRoom.SpecificInstancesPot[gobject.link_original.name].append(Instance)
        RsContainers.RsRoom.EveryInstancesPot.append(Instance)
        return Instance
    else:
        return None


def instance_create(gobject, layer, x = 0, y = 0):
    if RsContainers.RsRoom:
        Layer: Optional[RsLayer] = None
        if type(layer) is str:
            try:
                Layer = RsContainers.RsRoom.layer_find(layer)
            except KeyError:
                raise RuntimeError("The specific layer are not found.")
        elif type(layer) is RsLayer:
            Layer = layer
            
        print(Layer)
        if Layer:
            return instantiate(gobject, Layer, x, y)
    return None


def instance_destroy(instance: RsObject):
    instance.onDestroy()
    del instance
