from typing import Union

from .scene import RsScene
from .layer import RsLayer
from .prefab import RsPrefab, RsInstance, RsDirtyInstance
from .camera import RsCamera
from .sprite import RsImage, RsSprite
from .asset import *

from . import framework
from . import preset
from . import utility

GameObject = Union[RsInstance, RsDirtyInstance]
