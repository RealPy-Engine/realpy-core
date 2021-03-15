def test_main():
    import realpy

    Result: bool = True
    Result |= realpy.scene.test()
    Result |= realpy.layer.test()
    Result |= realpy.preset.test()
    Result |= realpy.utility.test()
    Result |= realpy.image.test()
    Result |= realpy.sprite.test()
    # Result |= realpy.prefab.test()
    # Result |= realpy.asset.test()

    return Result
