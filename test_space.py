import math
from realpy.layer import RsLayer

import realpy
from realpy import preset
from realpy import RsScene, RsPrefab, RsInstance, RsImage, RsSprite
from realpy import room_register, instance_create


class SPACESHIP_TYPES:
    PATROL = 0


class oTestRoom(RsScene):
    def __init__(self):
        super().__init__("roomTest")

    def onAwake(self):
        super().onAwake()
        print("Test initialized")

    def onUpdate(self, time):
        super().onUpdate(time)
        # print("Test updating")


class oSpaceShip(RsPrefab):
    @staticmethod
    def onUpdate(target, time):
        # print("Spaceship is updating")
        pass

    @staticmethod
    def onDraw(target, time):
        # TODO: #11 Make object can draw its sprite and can have dirty instance.
        if preset.application_surface and target.sprite_index:
            target.sprite_index.draw(preset.application_surface, 0, target.x, target.y)


if __name__ == "__main__":
    realpy.init("RealPy Engine", 640, 480)

    TestRoom = room_register(oTestRoom())

    Testbed = TestRoom.add_layer_direct(RsLayer("Instances"))
    TestRoom.add_layer_direct(RsLayer("Starfield"))
    TestRoom.add_layer_direct(RsLayer("Background"))
    print(repr(TestRoom))
    print(repr(Testbed))

    TestImage = RsImage("battleship.png")
    TestSprite = RsSprite(TestImage, 0)
    oSpaceShip.sprite_index = TestSprite
    TestInstance1 = oSpaceShip.instantiate(TestRoom, Testbed, 40, 40)
    print(repr(TestInstance1))

    realpy.startup()
