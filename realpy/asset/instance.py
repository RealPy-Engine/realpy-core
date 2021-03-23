import asyncio
from typing import List, Optional, Tuple, Type, Union

import pygame.mask as PyMask

from ..preset import RsPreset
from ..layer import RsLayer
from ..behavior import RsPrefab, RsActor, RsInstance
from ..utility import *


def collide_anyone(instance: RsInstance, prefab: Type[RsPrefab]) -> Optional[RsInstance]:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        return None

    if not instance.enabled or not instance.visible or not instance.can_collide or not instance.current_image:
        return None

    Checker = PyMask.from_surface(instance.current_image)
    CheckRect = instance.current_image.get_rect()
    CheckRect.x = int(instance.x)

    Other: RsInstance
    for Other in Pot:
        if Other == instance:
            continue
        if not Other.enabled or not Other.visible or not Other.can_collide or not Other.current_image:
            continue

        OtherChecker = PyMask.from_surface(Other.current_image)

        xOffset = int(Other.x - instance.x)
        yOffset = int(Other.y - instance.y)
        Result = Checker.overlap(OtherChecker, (xOffset, yOffset))
        if Result:
            return Other

    return None


def collide_all(instance: RsInstance, prefab: Type[RsPrefab]) -> Optional[List[RsInstance]]:
    ...


def actor_create(actor_type: Type[RsActor], layer_id: Union[str, RsLayer], x=0, y=0):
    """`actor_create(Scene, Layer)`
        ---
        Creates an simple behavior object.
    """

    if type(layer_id) is RsLayer:
        Place = layer_id
    else:
        try:
            Place = RsPreset.RsRoom.layer_find(str(layer_id))
        except KeyError:
            raise RuntimeError(f"The specific layer '{layer_id}' not found.")

    Instance = actor_type(Place.scene, Place)
    Method = Instance.onAwake
    if Method:
        Method()
    Place.add(Instance)

    return Instance


def instance_create(prefab: Type[RsPrefab], layer_id: Union[str, RsLayer], x=0, y=0):
    """`instance_create(Scene, Layer, x=0, y=0)`
        ---
        Creates an instance of game object.
    """

    if type(layer_id) is RsLayer:
        Place = layer_id
    else:
        try:
            Place = RsPreset.RsRoom.layer_find(str(layer_id))
        except KeyError:
            raise RuntimeError(f"The specific layer '{layer_id}' not found.")

    Instance = prefab.trait_instance(prefab, Place.scene, Place, x, y)
    Method = Instance.onAwake
    if Method:
        Method()
    Place.add(Instance)

    _instance_register(prefab, Instance)

    return Instance


def instance_number(prefab: Type[RsPrefab]) -> int:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        return 0
    return len(Pot)


def instance_find(prefab: Type[RsPrefab], index: int) -> Optional[RsInstance]:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        return None
    return Pot[index]


def _instance_register(prefab: Type[RsPrefab], instance: RsInstance):
    if issubclass(prefab, RsPrefab) and prefab is not RsPrefab:
        RsPreset.RsRoom.EveryInstancesPot.append(instance)
        instance.department.append(RsPreset.RsRoom.EveryInstancesPot)
        _instance_register_recursive(prefab, instance)


def _instance_register_recursive(prefab: Type[RsPrefab], instance: RsInstance):
    TempHash = hash(prefab)
    Where: List
    try:
        Where = RsPreset.RsRoom.SpecificInstancesPot[TempHash]
    except KeyError:
        RsPreset.RsRoom.SpecificInstancesPot[TempHash] = []
        Where = RsPreset.RsRoom.SpecificInstancesPot[TempHash]

    Where.append(instance)
    instance.attach(Where)

    Recursive_condition = (issubclass(prefab, RsPrefab) and prefab is not RsPrefab)
    if RsPreset.debug_get():
        print(Recursive_condition, "from", prefab)
        print(f"An instance is appended to {Where} of {prefab}.")
    if Recursive_condition:
        print("Goto ", prefab.__base__)
        _instance_register(prefab.__base__, instance)


def instance_destroy(target: Union[RsActor, RsInstance]):
    Method = target.onDestroy
    if Method:
        Method()
    del target
