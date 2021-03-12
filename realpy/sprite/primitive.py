import os
from typing import Union

import pygame.rect as PyRect
import pygame.image as PyImage
from pygame.surface import Surface as PySurface


class RsImage(object):
    """ RsImage(image_path)

        Raw image of a sprite that contains single image or multiple images.
    """

    def __init__(self, filepath: Union[str, list[str]]):
        self.number: int = -1
        self.raw_data: list[PySurface] = []
        self.boundbox = PyRect.Rect(0, 0, 0, 0)

        if type(filepath) is str:
            self.number = 0

            Temp = PyImage.load(filepath).convert_alpha()
            self.raw_data.append(Temp)
            self.filename = os.path.splitext(filepath)[0]
            self.boundbox = Temp.get_rect()
        elif type(filepath) is list[str]:
            self.number = len(filepath)

            for file in filepath:
                self.raw_data.append(PyImage.load(file).convert_alpha())
            self.filename = os.path.splitext(filepath[0])[0]

            Temp = PyImage.load(self.raw_data[0])
            self.boundbox = Temp.get_rect()

