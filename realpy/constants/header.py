# 10 px == 1 metre
phy_mess: float = 10.0 / 1
phy_velocity: float = (((1000.0 / 60.0) / 60.0) * phy_mess)

# Mouse buttons
MB_LEFT = 1
MB_MIDDLE = 2
MB_RIGHT = 3

# Virtual keys
VK_ESCAPE = 27
VK_SPACE = 32
VK_A = 97


class INPUT_STATES:
    NONE = 0
    PRESSED = 1
    ING = 2
    RELEASED = 3


class MASKS:
    RECTANGLE = 0
    CIRCLE = 2
