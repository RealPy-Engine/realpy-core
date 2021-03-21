import realpy

from realpy import (
    RsScene, RsLayer, RsPrefab, RsImage, RsSprite, RsPreset, room_register, instance_create
)


if __name__ == "__main__":
    # TODO: #17 Make easy to create user's custom preset.
    realpy.init("RealPy Engine", 640, 480)
    realpy._debug_set(True)

    TestImage = RsImage("test_battleship.png")
    TestSprite = RsSprite(TestImage, 0, 50, 24)


    class oTestRoom(RsScene):
        def onAwake(self):
            super().onAwake()
            print("Test initialized")

        def onUpdate(self, time):
            super().onUpdate(time)


    class oSpaceShip(RsPrefab):
        pass


    class oEnemyParent(oSpaceShip):
        pass


    class oEnemyBattleship(oEnemyParent):
        sprite_index = TestSprite

        @staticmethod
        def onAwake(itself) -> None:
            # itself.speed = 70
            # itself.direction = 200
            # itself.friction = 10
            # itself.image_angle = itself.direction
            pass
        
        @staticmethod
        def onUpdate(itself, time):
            if 0 < itself.speed:
                print("Speed: ", itself.speed, " Vspeed: ", itself.vspeed)
            itself.image_angle += 30 * time


    Temp = oTestRoom()
    TestRoom = room_register(Temp, "roomTest")

    Testbed = TestRoom.add_layer_direct(RsLayer("Instances"))
    TestRoom.add_layer_direct(RsLayer("Starfield"))
    TestRoom.add_layer_direct(RsLayer("Background"))

    instance_create(oEnemyBattleship, Testbed, 320, 240)
    # instance_create(oEnemyBattleship, Testbed, 240, 240)
    # instance_create(oEnemyBattleship, Testbed, 400, 240)

    realpy.startup()
