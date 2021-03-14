from typing import Union

from .scene import RsScene
from .layer import RsLayer
from .prefab import RsPrefab, RsInstance
from .camera import RsCamera
from .image import RsImage
from .sprite import RsSprite

from . import framework
from . import preset

from . import utility as RsUtility

from .asset import *


init = framework.rs_init
startup = framework.rs_startup
quit = framework.rs_quit
