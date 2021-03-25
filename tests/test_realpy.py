import realpy


def test_main():
    assert realpy.framework.test()
    assert realpy.scene.test()
    assert realpy.image.test()
    assert realpy.sprite.test()
    print("***** Realpy Test Finished *****")


if __name__ == "__main__":
    test_main()
