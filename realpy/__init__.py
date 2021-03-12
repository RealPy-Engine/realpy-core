from typing import Union

from .scene import RsScene
from .layer import RsLayer
from .prefab import RsPrefab, RsInstance
from .camera import RsCamera
from .sprite import RsImage, RsSprite

from . import framework
from . import preset

from .asset import *
from .utility import *


init = framework.rs_init
startup = framework.rs_startup
quit = framework.rs_quit
