import RsCore
from RsCore.assets import room_register, instance_create

from RsCore.prefab import RsPrefab
from RsCore.instance import RsDirtyObject


class preTest(RsPrefab):
    name = "preTest"
    pass


#TestPrefab = preTest("preTest")


class oTest(RsDirtyObject):
    link_original = preTest


if __name__ == "__main__":
    RsCore.init("RealPy Engine", 640, 480)

    TestRoom = room_register("roomTest")

    Testbed = TestRoom.add_layer("Instances")
    TestRoom.add_layer("Background")

    TestInstance1 = instance_create(oTest, Testbed, 40, 40)
    print(TestInstance1)
    TestInstance2 = oTest(TestRoom, Testbed, 80, 40)
    print(TestInstance2)

    RsCore.startup()
