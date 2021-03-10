from realpy import framework
from realpy.asset import room_register, instance_create
from realpy.prefab import RsPrefab


class oTest(RsPrefab):
    pass


if __name__ == "__main__":
    framework.rs_init("RealPy Engine", 640, 480)

    TestRoom = room_register("roomTest")
    Testbed = TestRoom.add_layer("Instances")
    TestRoom.add_layer("Background")

    TestInstance1 = instance_create(oTest, Testbed, 40, 40)
    print(TestInstance1)
    print(TestInstance1.original)
    TestInstance2 = oTest.instantiate_complex(TestRoom, Testbed, 80, 40)
    print(TestInstance2)
    print(TestInstance2.original)

    framework.rs_startup()

