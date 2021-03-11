import os
from typing import Optional

from pygame.sprite import Sprite as PySprite
import pygame.image as PyImage
import pygame.rect as PyRect
from pygame.surface import Surface


class RsImage(object):
    def __init__(self, filepath) -> None:
        self.number = -1
        self.raw_data = []
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


class RsSprite(object):
    def __init__(self, image, mask_type, xo=0, yo=0):
        self.image: Optional[RsImage] = image
        self.xoffset = xo
        self.yoffset = yo
        self.mask_type = mask_type

    def draw(self, where, index, x, y):
        # TODO: #10 Game object still can't draw its sprite.
        if self.image:
            if self.image.number == 0:
                Image: Surface = self.image.raw_data[0]
                Position = Image.get_rect()
                Position.center = (x, y)
                #Position.x = x
                #Position.y = y
                Image.blit(where, Position)
            elif 0 < self.image.number:
                Image: Surface = self.image.raw_data[index]
                Position = Image.get_rect()
                Position.x = x
                Position.y = y
                Image.blit(where, Position)


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
