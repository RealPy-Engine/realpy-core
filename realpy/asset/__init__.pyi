from typing import Optional, Union

from realpy import GameObject
from realpy import RsScene
from realpy import RsLayer
from realpy import RsDirtyInstance, RsPrefab, RsInstance

__all__ = [
    "object_register",
    "scene_update", "room_register", "room_get", "room_goto", "room_goto_next",
    "global_layer_find",
    "instance_create", "instance_destroy"
]


def object_register(prefab: type[RsPrefab]) -> type[RsPrefab]:
    ...


async def scene_update(room: RsScene, time: int) -> None:
    ...


def room_register(info: Union[RsScene, str]) -> RsScene:
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


def instantiate(gobject: type[RsPrefab], layer: RsLayer, x: float = 0, y: float = 0) -> GameObject:
    ...


def instance_create(gobject: type[RsPrefab], layer: Union[str, RsLayer], x: float = 0, y: float = 0) -> GameObject:
    ...


def instance_destroy(target: GameObject) -> None:
    ...
