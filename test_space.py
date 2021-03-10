import math

from realpy import framework, preset
from realpy import RsPrefab, RsInstance, RsDirtyInstance, RsImage, RsSprite
from realpy import room_register, instance_create


class SPACESHIP_TYPES:
    PATROL = 0


class oSpaceShip(RsPrefab):
    @staticmethod
    def onDraw(target: RsDirtyInstance, time):
        super().onDraw(target, time)
        if preset.RsScreen and target.sprite_index:
            target.sprite_index.draw(preset.RsScreen, math.floor(target.image_index), target.x, target.y)


if __name__ == "__main__":
    framework.rs_init("RealPy Engine", 640, 480)

    TestRoom = room_register("roomTest")
    Testbed = TestRoom.add_layer("Instances")
    Testbed = TestRoom.add_layer("Starfield")
    TestRoom.add_layer("Background")

    TestImage = RsImage("battleship.png")
    TestSprite = RsSprite(TestImage, 0)

    TestInstance1 = instance_create(oSpaceShip, Testbed, 40, 40)

    print(TestInstance1)
    print(TestInstance1.original)
    # print(repr(oSpaceShip()))

    framework.rs_startup()
