from pygame.surface import Surface
from pygame import transform
from numpy.matrixlib import mat

__all__ = ["RsSprite"]


class RsSprite(object):
    """`RsSprite(image, mask_type, x_offset, y_offset)`
        ---
        Advance asset of image.
    """

    __slots__ = ["image", "mask_type", "width", "height", "radius", "xoffset", "yoffset", "boundbox"]

    def __init__(self, image, mask_type: int = 0, xo: int = 0, yo: int = 0):
        self.image = image
        self.mask_type: int = mask_type
        self.width: int = image.boundbox.width
        self.height: int = image.boundbox.height
        self.radius: int = max(xo, yo)
        self.xoffset: int = xo
        self.yoffset: int = yo

        bx, bex = -xo, self.width - xo
        by, bey = -yo, self.height - yo
        self.boundbox = [(bx, by), (bex, by), (bx, bey), (bex, bey)]

    def draw(self, where: Surface, index, x, y, scale: float = 1, orientation: float = 0,
             alpha: float = 1):
        if 0 == scale or alpha <= 0:
            return
        if self.image:
            if 0 < self.image.number:
                index = index % self.image.number
                Frame: Surface = self.image.raw_data[index]
                OrgPosition = self.image.boundbox

                # TODO: Use negative scale for drawing sprite.
                Sizes = (int(scale * Frame.get_width()), int(scale * Frame.get_height()))
                Trx: Surface
                Trx = transform.scale(Frame, Sizes)
                
                if orientation != 0:
                    Trx = transform.rotate(Trx, orientation)
                #Trx = transform.rotozoom(Frame, orientation, scale)

                Position = Trx.get_rect()
                Position.center = (x, y)
                where.blit(Trx, Position)


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
