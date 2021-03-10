import os

import pygame.image as PyImage
import pygame.rect as PyRect


class RsImage(object):
    boundbox = PyRect.Rect(0, 0, 0, 0)

    def __init__(self, filepath) -> None:
        if not PyImage.get_extended():
            raise RuntimeError("Cannot load image files.")

        self.number = -1
        self.raw_data = []

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
    def __init__(self, image, mask_type, xo=0, yo=0):
        self.raw_data = image
        self.xoffset = xo
        self.yoffset = yo

    def update(self, x, y):
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
