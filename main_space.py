import realpy

from realpy import (
    RsScene, RsLayer, RsPrefab, RsImage, RsSprite, RsPreset, room_register, instance_create
)


class SPACESHIP_TYPES:
    PATROL = 0


if __name__ == "__main__":
    # TODO: #17 Make easy to create user's custom preset.
    realpy.init("RealPy Engine", 640, 480)
    RsPreset.debug = True

    TestImage = RsImage("test_battleship.png")
    TestSprite = RsSprite(TestImage, 0, 50, 24)


    class oTestRoom(RsScene):
        def onAwake(self):
            super().onAwake()
            print("Test initialized")

        def onUpdate(self, time):
            super().onUpdate(time)


    class oSpaceShip(RsPrefab):
        sprite_index = TestSprite

        @staticmethod
        def onAwake(itself) -> None:
            itself.speed = 20
            itself.direction = 315
            # itself.friction = 5
            itself.image_angle = 315
        
        @staticmethod
        def onUpdate(itself, time):
            if 0 < itself.speed:
                print("Speed: ", itself.speed, " Vspeed: ", itself.vspeed)
            #itself.image_angle += 30 * time


    Temp = oTestRoom()
    TestRoom = room_register(Temp, "roomTest")

    Testbed = TestRoom.add_layer_direct(RsLayer("Instances"))
    TestRoom.add_layer_direct(RsLayer("Starfield"))
    TestRoom.add_layer_direct(RsLayer("Background"))

    instance_create(oSpaceShip, Testbed, 320, 240)
    # instance_create(oSpaceShip, Testbed, 240, 240)
    # instance_create(oSpaceShip, Testbed, 400, 240)

    realpy.startup()
