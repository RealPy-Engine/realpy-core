from typing import List, Optional, Type, Union

import pygame.mask as PyMask

from ..behavior import RsPrefab, RsActor, RsInstance
from ..layer import RsLayer
from ..preset import RsPreset


def collide_anyone(instance: RsInstance, prefab: Type[RsPrefab]) -> Optional[RsInstance]:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.room.SpecificInstancesPot[TempHash]
    except KeyError:
        return None

    if not instance.enabled or not instance.visible or not instance.can_collide or not instance.current_image:
        return None

    Checker = PyMask.from_surface(instance.current_image)

    Other: RsInstance
    for Other in Pot:
        if Other == instance:
            continue
        if not Other.enabled or not Other.visible or not Other.can_collide or not Other.current_image:
            continue

        OtherChecker = PyMask.from_surface(Other.current_image)
        Check = Checker.overlap(OtherChecker, (int(Other.x - instance.x), int(Other.y - instance.y)))
        if Check:
            return Other

    return None


def collide_all(instance: RsInstance, prefab: Type[RsPrefab]) -> Optional[List[RsInstance]]:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.room.SpecificInstancesPot[TempHash]
    except KeyError:
        return None

    if len(Pot) == 0 or not instance.enabled or not instance.visible or not instance.can_collide or not \
            instance.current_image:
        return None

    Result: List[RsInstance] = []
    Checker = PyMask.from_surface(instance.current_image)

    Other: RsInstance
    for Other in Pot:
        if Other == instance:
            continue
        if not Other.enabled or not Other.visible or not Other.can_collide or not Other.current_image:
            continue

        OtherChecker = PyMask.from_surface(Other.current_image)
        Check = Checker.overlap(OtherChecker, (int(Other.x - instance.x), int(Other.y - instance.y)))
        if Check:
            Result.append(Other)

    return Result


def actor_create(actor_type: Type[RsActor], layer_id: Optional[Union[str, RsLayer]]) -> RsActor:
    """`actor_create(Scene, Layer)`
        ---
        Creates an simple behavior object.
    """

    Instance: RsActor
    if layer_id:
        Place: Optional[RsLayer]
        if isinstance(layer_id, RsLayer):
            Place = layer_id
        else:
            Place = RsPreset.room.layer_find(str(layer_id))

        if Place:
            Instance = actor_type(Place)
            Method = Instance.onAwake
            if Method:
                Method()
            Place.add(Instance)
        else:
            raise RuntimeError("The specific layer not exists.")
    else:
        Instance = actor_type(None)
        Method = Instance.onAwake
        if Method:
            Method()

    return Instance


def instance_create(prefab: Type[RsPrefab], layer_id: Optional[Union[str, RsLayer]], x=0, y=0) -> RsInstance:
    """`instance_create(Scene, Layer, x=0, y=0)`
        ---
        Creates an instance of game object.
    """

    Instance: RsInstance
    if layer_id:
        Place: Optional[RsLayer]
        if isinstance(layer_id, RsLayer):
            Place = layer_id
        else:
            Place = RsPreset.room.layer_find(str(layer_id))

        if Place:
            Instance = prefab.trait_instance(prefab, Place, x, y)
            Place.add(Instance)
        else:
            raise RuntimeError(f"The specific layer '{layer_id}' not found.")
    else:
        Instance = prefab.trait_instance(prefab, None, x, y)

    Method = Instance.onAwake
    if Method:
        Method()

    _instance_register(prefab, Instance)

    return Instance


def instance_number(prefab: Type[RsPrefab]) -> int:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.room.SpecificInstancesPot[TempHash]
    except KeyError:
        return 0
    return len(Pot)


def instance_find(prefab: Type[RsPrefab], index: int) -> Optional[RsInstance]:
    TempHash = hash(prefab)
    Pot: List
    try:
        Pot = RsPreset.room.SpecificInstancesPot[TempHash]
    except KeyError:
        return None
    return Pot[index]


def _instance_register(prefab: Type[RsPrefab], instance: RsInstance):
    if issubclass(prefab, RsPrefab) and prefab is not RsPrefab:
        instance.attach(RsPreset.room.EveryInstancesPot)
        _instance_register_recursive(prefab, instance)


def _instance_register_recursive(prefab: Type[RsPrefab], instance: RsInstance):
    TempHash = hash(prefab)
    Where: List
    try:
        Where = RsPreset.room.SpecificInstancesPot[TempHash]
    except KeyError:
        RsPreset.room.SpecificInstancesPot[TempHash] = []
        Where = RsPreset.room.SpecificInstancesPot[TempHash]

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
