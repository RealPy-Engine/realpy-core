from typing import Optional, Union, Type

from realpy.scene import RsScene
from realpy.layer import RsLayer
from realpy.prefab import RsPrefab, RsInstance

__all__ = [
    "object_register",
    "scene_update", "room_register", "room_get", "room_goto", "room_goto_next",
    "global_layer_find",
    "instance_create", "instance_destroy"
]


def object_register(prefab: Type[RsPrefab]) -> Type[RsPrefab]:
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


def instantiate(gobject: Type[RsPrefab], layer: RsLayer, x: float = 0, y: float = 0) -> RsInstance:
    ...


def instance_create(gobject: Type[RsPrefab], layer: Union[str, RsLayer], x: float = 0, y: float = 0) -> RsInstance:
    ...


def instance_destroy(target: RsInstance) -> None:
    ...
