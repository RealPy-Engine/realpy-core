from RsCore.scene import RsScene
from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.instance import RsObject
from RsCore.sprite import RsSprite
from RsCore import constants as RsConstants, containers as RsContainers
from RsCore.assets import room_register, instance_create

def init():
    # Test
    from .spaceships import oSpaceShip
    TestInstance = instance_create(oSpaceShip, "Instances", 0, 50)
    print(TestInstance)


