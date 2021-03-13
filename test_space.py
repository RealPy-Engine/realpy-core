import math
from realpy.layer import RsLayer

import realpy
from realpy import preset
from realpy import RsScene, RsPrefab, RsInstance, RsImage, RsSprite
from realpy import room_register, instance_create


class SPACESHIP_TYPES:
    PATROL = 0


if __name__ == "__main__":
    # TODO: #17 Make easy to create user's custom preset.
    realpy.init("RealPy Engine", 640, 480)

    TestImage = RsImage("battleship.png")
    TestSprite = RsSprite(TestImage, 0)


    class oTestRoom(RsScene):
        def onAwake(self):
            super().onAwake()
            print("Test initialized")

        def onUpdate(self, time):
            super().onUpdate(time)
            # print("Test updating")


    class oSpaceShip(RsPrefab):
        sprite_index = TestSprite


    Temp = oTestRoom()
    TestRoom = room_register(Temp, "roomTest")

    Testbed = TestRoom.add_layer_direct(RsLayer("Instances"))
    TestRoom.add_layer_direct(RsLayer("Starfield"))
    TestRoom.add_layer_direct(RsLayer("Background"))
    print(repr(TestRoom))
    print(repr(Testbed))

    TestInstance1 = instance_create(oSpaceShip, Testbed, 40, 40)
    print(repr(Testbed))
    print(repr(TestInstance1))

    realpy.startup()
