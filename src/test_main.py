import RsCore


if __name__ == "__main__":
    RsCore.init("RealPy Engine", 640, 480)
    TestRoom = RsCore.room_register("roomTest")
    TestRoom.add_layer("Instances")
    TestRoom.add_layer("Background")
    RsCore.startup()
