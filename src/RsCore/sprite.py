import os
from typing import Optional, Union

import pygame.image as PyImage
import pygame.rect as PyRect
from pygame.surface import Surface as PySurface

import RsCore.constants as RsConstants


class RsImage(object):
    """
        RsImage(image_path)

        Raw image of a sprite that contains single image or multiple images.
    """
    boundbox = PyRect.Rect(0, 0, 0, 0)

    def __init__(self, filepath: Union[list[str], str]) -> None:
        if not PyImage.get_extended():
            raise RuntimeError("Cannot load image files.")

        self.number: int
        self.raw_data: list[PySurface] = []

        if type(filepath) is str:
            self.number = 0
            self.raw_data.append(PyImage.load(filepath))
            # TODO: #8 can't find the image file
            self.filename = os.path.splitext(filepath)[0]
        else:
            self.number = len(filepath)

            for file in filepath:
                self.raw_data.append(PyImage.load(file))
            self.filename = os.path.splitext(filepath[0])[0]

        self.boundbox.width = self.raw_data[0].get_width()
        self.boundbox.height = self.raw_data[0].get_height()


class RsSprite(object):
    raw_data: Optional[RsImage] = None
    xoffset: int = 0
    yoffset: int = 0

    def __init__(self, image: RsImage, mask_type=RsConstants.MASKS.RECTANGLE, xo: int = 0, yo: int = 0):
        self.raw_data = image
        self.xoffset = xo
        self.yoffset = yo

    def update(self, x: float, y: float):
        if self.raw_data:
            Box = self.raw_data.boundbox
            Box.x = int(x)
            Box.y = int(y)


"""
def sprite_json_loads():
    try:
        with open("Data\\sprite.json") as sprfile:
            parsed = json.load(sprfile)

            for content in parsed:
                sprite_load(content["path"], content["name"], content["xoffset"], content["yoffset"], content["number"])

    except FileNotFoundError:
        pass
"""
