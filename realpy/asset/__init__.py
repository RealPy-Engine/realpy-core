""" Asset Management
    ---
    ```
    import realpy
    realpy.method()
    ```
"""
from .instance import (
    instance_create, instance_destroy, instance_number, instance_find,
    actor_create,
    collide_anyone, collide_all
)
from .room import (
    room_register, room_get, room_goto, room_goto_next
)
