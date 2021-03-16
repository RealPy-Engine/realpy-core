def test_main():
    from .. import realpy

    assert realpy.framework.test()
    assert realpy.scene.test()
    assert realpy.layer.test()
    assert realpy.preset.test()
    assert realpy.utility.test()
    assert realpy.image.test()
    assert realpy.sprite.test()
    assert realpy.utility.test()
    print("***** Realpy Test Finished *****")


if __name__ == "__main__":
    test_main()
