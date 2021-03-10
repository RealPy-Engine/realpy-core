from typing import Optional, Union

import pygame.image as PyImage
import pygame.rect as PyRect
from pygame.surface import Surface as PySurface

from realpy import preset


class RsImage(object):
    """
        RsImage(image_path)

        Raw image of a sprite that contains single image or multiple images.
    """
    number: int
    boundbox: PyRect.Rect
    raw_data: list[PySurface]

    def __init__(self, filepath: Union[str, list[str]]) -> None:
        ...

    ...


class RsSprite(object):
    image: Optional[RsImage]
    xoffset: int
    yoffset: int

    def __init__(self, image: RsImage, mask_type=preset.MASKS.RECTANGLE, xo: int = 0, yo: int = 0):
        self.image: Optional[RsImage]
        ...

    def update(self, x: float, y: float):
        ...

    def draw(self, where: PySurface, index: int, x: float, y: float):
        ...

    ...
