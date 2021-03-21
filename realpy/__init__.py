from .framework import RsFramework
from .scene import RsScene
from .layer import RsLayer
from .image import RsImage
from .sprite import RsSprite
from .prefab import RsGameObject

from .preset import *
from .utility import *
from .asset import *

init = RsFramework.rs_init
startup = RsFramework.rs_startup
quit = RsFramework.rs_quit
