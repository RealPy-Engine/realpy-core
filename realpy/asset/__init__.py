""" Asset Management
    ---
    ```
    import realpy
    realpy.method()
    ```
"""
from .room import (
    room_register, room_get, room_goto, room_goto_next
)

from .instance import (
    instance_create, instance_destroy
)

# TODO: #21 Make a test from assets.
def test():
    pass
