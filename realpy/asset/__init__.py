from realpy.scene import RsScene
from realpy import preset


def object_register(prefab):
    preset.PrefabsPot.append(prefab)
    return prefab


def room_register(name):
    NewRoom = RsScene(name)

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
    preset.RoomPot[name] = NewRoom
    return NewRoom


def room_get(id):
    if type(id) is int:
        return preset.RoomOrder[id]
    elif type(id) is str:
        return preset.RoomPot[id]


def room_set(taget):
    if preset.RsRoom:
        preset.RsRoom.onDestroy()
    preset.RsRoom = taget
    preset.RsRoom.onAwake()
    print("Go to " + str(preset.RsRoom))


def room_goto(name):
    Temp = room_get(name)
    if not Temp:
        raise RuntimeError("The room " + name + " doesn't exist.")
    elif Temp is not preset.RsRoom:
        room_set(Temp)


def room_goto_next():
    Next = preset.RsRoom.next
    print(Next)
    if Next:
        room_set(Next)
    else:
        raise RuntimeError("The next room doesn't exist.\n")


def global_layer_find(name):
    if preset.RsRoom:
        Where = preset.RsRoom.trees[name]
        return Where
    return None


def make_instance(gobject, layer, x=0, y=0):
    if preset.RsRoom:
        Instance = gobject.instantiate(preset.RsRoom, layer, x, y)
        Instance.onAwake()

        TempHash = hash(gobject)
        try:
            if not preset.RsRoom.SpecificInstancesPot[TempHash]:
                preset.RsRoom.SpecificInstancesPot[TempHash] = []
        except KeyError:
            preset.RsRoom.SpecificInstancesPot[TempHash] = []
        finally:
            preset.RsRoom.SpecificInstancesPot[TempHash].append(Instance)
        return Instance
    else:
        raise RuntimeError("No scene exists.")


def instance_create(gobject, layer, x=0, y=0):
    if preset.RsRoom:
        if not layer:
            raise RuntimeError("No layer specified.")
        if type(layer) is str:
            try:
                Layer = preset.RsRoom.layer_find(layer)
            except KeyError:
                raise RuntimeError("The specific layer are not found.")
        else:
            Layer = layer

        print(Layer)
        return make_instance(gobject, Layer, x, y)
    return None


def instance_destroy(target):
    target.onDestroy()
    del target
