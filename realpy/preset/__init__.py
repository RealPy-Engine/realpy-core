from pygame import Color


Resolutions = (640, 480)

# Application surface
RsScreen = None

# Rooms
RsRoom = None
RsLastRoom = None
RoomOrder = []
RoomPot = {}

# Events
Events = []

# Sprite texture group
Atlas = []

# All game objects
PrefabsPot = []

# All sounds
AudioPot = {}

# 10 px == 1 metre
phy_mess = 10.0 / 1
phy_velocity = (((1000.0 / 60.0) / 60.0) * phy_mess)

# Colors
# 1
c_white = Color(255, 255, 255)
c_ltgray = Color(192, 192, 192)
c_gray = Color(128, 128, 128)
c_dkgray = Color(64, 64, 64)
c_black = Color(0, 0, 0)

# 2
c_red = Color(255, 0, 0)
c_lime = Color(0, 255, 0)
c_green = Color(0, 128, 0)
c_blue = Color(0, 0, 255)

# 3
c_maroon = Color(128, 0, 0)
c_dkrose = Color(64, 0, 0)
c_dkgreen = Color(0, 64, 0)
c_ultramarine = Color(0, 0, 128)
c_navy = Color(0, 0, 96)

# 4
c_yellow = Color(255, 255, 0)
c_fuchsia = Color(255, 0, 255)
c_aqua = Color(0, 255, 255)

# 5
c_orange = Color(255, 128, 0)
c_cyan = Color(0, 128, 255)
c_magenta = Color(255, 0, 128)
c_purple = Color(128, 0, 255)
c_teal = Color(0, 255, 128)


class MASKS:
    RECTANGLE = 0
    CIRCLE = 2
