from .framework import RsFramework
from .preset import RsPreset
from .scene import RsScene
from .layer import RsLayer
from .image import RsImage
from .sprite import RsSprite
from .prefab import RsPrefab, RsInstance
from .utility import RsUtility
from .asset import *

init = RsFramework.rs_init
startup = RsFramework.rs_startup
quit = RsFramework.rs_quit
