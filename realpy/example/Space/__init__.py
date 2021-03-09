import RsCore
from RsCore.assets import room_register, instance_create
from RsCore.prefab import RsPrefab
from RsCore.sprite import RsImage, RsSprite


class SPACESHIP_TYPES:
    PATROL = 0


class oSpaceShip(RsPrefab):
    pass


if __name__ == "__main__":
    RsCore.init("RealPy Engine", 640, 480)

    TestRoom = room_register("roomTest")
    Testbed = TestRoom.add_layer("Instances")
    Testbed = TestRoom.add_layer("Starfield")
    TestRoom.add_layer("Background")
    
    TestImage = RsImage("battleship.png")
    TestSprite = RsSprite(TestImage)

    TestInstance1 = instance_create(oSpaceShip, Testbed, 40, 40)
    

    print(TestInstance1)
    print(TestInstance1.original)

    RsCore.startup()
