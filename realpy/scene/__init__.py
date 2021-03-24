""" Scene
    ---
    ```
    from realpy import RsScene
    ```
"""
from .header import RsScene

__all__ = ["RsScene"]


def test():
    print("***** Test → Realpy Scene *****")

    from realpy.behavior.instance import RsInstance
    from realpy import RsLayer

    try:
        print(">>> Class of scene: ", RsScene)
        print(">>> Class of layer: ", RsLayer)

        Sample = RsScene()
        SampleLayers = [RsLayer("First"), RsLayer("Second"), RsLayer("Third")]
        print("Sample scene: ", Sample)
        print("Sample layer group: ", SampleLayers)

        for Item in SampleLayers:
            Sample.add_layer_direct(Item)
        SampleSeek = Sample.layer_find("First")
        print("Found scene (maybe 'First'): ", SampleSeek)
        SampleSeek = Sample.layer_find("Fourth")
        print("Found scene (maybe 'None'): ", SampleSeek)

        Sample.add_layer_direct(RsLayer("Fifth"))
        print("The layers: ", Sample.layer_stack)

        Sample.onAwake()
    except KeyError as e:
        print("Key Error: ", e)
        return False
    except AttributeError as e:
        print("Attribute Error: ", e)
        return False
    except Exception as e:
        print("Error: ", e)
        return False
    return True
