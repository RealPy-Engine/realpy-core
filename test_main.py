import realpy
from realpy import RsScene, RsLayer, RsPrefab
from realpy import room_register, instance_create


class oTest(RsPrefab):
    pass


if __name__ == "__main__":
    realpy.init("RealPy Engine", 640, 480)

    TestRoom = room_register(RsScene("roomTest"))
    Testbed = TestRoom.add_layer_direct(RsLayer("Instances"))
    TestRoom.add_layer_direct(RsLayer("Background"))

    TestInstance1 = instance_create(oTest, Testbed, 40, 40)
    print(TestInstance1)
    print(TestInstance1.original)
    TestInstance2 = oTest.instantiate(TestRoom, Testbed, 80, 40)
    print(TestInstance2)
    print(TestInstance2.original)

    realpy.startup()

