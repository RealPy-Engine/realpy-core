import pygame.constants as PyConstants


# 10 px == 1 metre
phy_mess: float = 10.0 / 1
phy_velocity: float = (((1000.0 / 60.0) / 60.0) * phy_mess)


class MASKS:
    RECTANGLE: int = 0
    CIRCLE: int = 2
