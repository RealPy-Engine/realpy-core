import math
from realpy.scene import RsScene

from realpy import framework, preset
from realpy import RsPrefab, RsInstance, RsDirtyInstance, RsImage, RsSprite
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
    __is_dirty = True

    @staticmethod
    def onUpdate(target, time):
        print("Spaceship is updating")

    @staticmethod
    def onDraw(target, time):
        print(super)
        print(target, time)
        # TODO: #11 Make object can draw its sprite and can have dirty instance.
        if preset.RsScreen and target.sprite_index:
            print(target.sprite_index)
            target.sprite_index.draw(preset.RsScreen, 0, target.x, target.y)


if __name__ == "__main__":
    framework.rs_init("RealPy Engine", 640, 480)

    TestRoom = room_register(oTestRoom())
    Testbed = TestRoom.add_layer("Instances")
    TestRoom.add_layer("Starfield")
    TestRoom.add_layer("Background")
    print(repr(TestRoom))
    print(repr(Testbed))

    TestImage = RsImage("battleship.png")
    TestSprite = RsSprite(TestImage, 0)

    TestInstance1 = oSpaceShip.make_instance_complex(TestRoom, Testbed, 40, 40)

    framework.rs_startup()
