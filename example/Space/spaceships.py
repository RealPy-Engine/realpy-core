from RsCore.prefab import RsPrefab
from RsCore.instance import RsDirtyObject


class SPACESHIP_TYPES:
    PATROL = 0


class preSpaceShip(RsPrefab):
    pass


class oSpaceShip(RsDirtyObject):
    link_original = preSpaceShip
