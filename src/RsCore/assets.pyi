from typing import Optional, Union, Type

from RsCore.scene import RsScene
from RsCore.layer import RsLayer
from RsCore.prefab import RsPrefab
from RsCore.instance import RsObject
from RsCore import constants as RsConstants, containers as RsContainers

__all__ = [
    "object_register",
    "scene_update", "room_register", "room_get", "room_goto", "room_goto_next",
    "global_layer_find",
    "instance_create", "instance_destroy"
]


def object_register(name: str) -> RsPrefab:
    ...


async def scene_update(room: RsScene, time: int) -> None:
    ...


def room_register(name: str) -> RsScene:
    ...


def room_get(id: Union[int, str]) -> Optional[RsScene]:
    ...


def room_set(taget: RsScene) -> None:
    ...


def room_goto(name: str) -> None:
    ...


def room_goto_next() -> None:
    ...


def global_layer_find(name: str) -> Optional[RsLayer]:
    ...


def instantiate(gobject: Type[RsObject], layer: RsLayer, x: float = 0, y: float = 0) -> RsObject:
    ...


def instance_create(gobject: Type[RsObject], layer: Union[str, RsLayer], x: float = 0, y: float = 0) -> RsObject:
    ...


def instance_destroy(instance: RsObject) -> None:
    ...
