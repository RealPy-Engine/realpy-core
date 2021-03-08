from ..src import RsCore


if __name__ == "__main__":
    RsCore.init("RealPy Engine", 640, 480)
    RsCore.room_register("roomTest")
    RsCore.startup()
