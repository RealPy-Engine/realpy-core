from typing import Type

from .backend import RsGameObject
from .instance import RsInstance


class RsPrefab(object):
    """`RsPrefab`
        ---
        Big behavior object.
    """

    type_api: Type = RsGameObject
    type_instance: Type = RsInstance
