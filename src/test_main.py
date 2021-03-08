import RsCore
from RsCore.assets import room_register, instance_create

from RsCore.prefab import RsPrefab
from RsCore.instance import RsDirtyObject


class preSpaceShip(RsPrefab):
    pass


class oSpaceShip(RsDirtyObject):
    link_original = preSpaceShip


if __name__ == "__main__":
    RsCore.init("RealPy Engine", 640, 480)

    # TODO: Layer and instances don't work
    TestRoom = room_register("roomTest")

    Testbed = TestRoom.add_layer("Instances")
    TestRoom.add_layer("Background")

    TestInstance1 = instance_create(oSpaceShip, Testbed, 40, 40)
    print(TestInstance1)
    TestInstance2 = oSpaceShip(TestRoom, Testbed, 80, 40)
    print(TestInstance2)

    RsCore.startup()
