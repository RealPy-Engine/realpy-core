from typing import Optional

from pygame.surface import Surface

from .primitive import RsImage

__all__ = ("RsImage", "RsSprite")


class RsSprite(object):
    def __init__(self, image: RsImage, mask_type: int=0, xo: int=0, yo: int=0):
        self.image: Optional[RsImage] = image
        self.mask_type: int = mask_type
        self.xoffset: int = xo
        self.yoffset: int = yo

    def draw(self, where, index, x: int, y: int, xscale: float=1, yscale: float=1, orientation: float=0, blend: int=0, alpha: float=1):
        # TODO: #10 Game object still can't draw its sprite.
        if self.image:
            if self.image.number == 0:
                Image: Surface = self.image.raw_data[0]
                Position = Image.get_rect()
                Position.center = (x, y)
                where.blit(Image, Position)
            elif 0 < self.image.number:
                Image: Surface = self.image.raw_data[index]
                Position = Image.get_rect()
                Position.center = (x, y)
                where.blit(Image, Position)


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
