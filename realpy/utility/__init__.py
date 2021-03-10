import math
import random


def sqr(v):
    return v * v


def sign(x):
    ret = 0
    if x > 0:
        ret = 1
    elif x < 0:
        ret = - 1
    return ret


def degtorad(degree):
    return math.radians(degree * math.pi / 180)


def radtodeg(radian):
    return math.degrees(radian)


def bezier4(t, x1, x2, x3, x4):
    factor = 1 - t

    return factor * (factor * (factor * x1 + t * x2)
                     + t * (factor * x2 + t * x3)) + t * (factor * (factor * x2 + t * x3) + t * (factor * x3 + t * x4))


def lengthdir_x(length, direction):
    return math.cos(degtorad(direction)) * length


def lengthdir_y(length, direction):
    return -math.sin(degtorad(direction)) * length


def point_distance(X1, Y1, X2, Y2):
    return math.dist([X1, Y1], [X2, Y2])


def point_direction(X1, Y1, X2, Y2):
    return radtodeg(math.atan2(Y2 - Y1, X1 - X2))


def irandom(n):
    return random.randint(0, int(n))


def irandom_range(n1, n2):
    return random.randint(int(n1), int(n2))


def distribute(x1, x2, ratio):
    if irandom(100) <= ratio * 100:
        return x1
    else:
        return x2


def probability_test(max):
    return bool(irandom(max - 1) == 0)


def choose(*args):
    length = len(args)
    if length <= 0:
        raise RuntimeError("choose 함수에 값이 제대로 전달되지 않았습니다!" + __name__)

    pick = None
    try:
        pick = args[irandom(length - 1)]
    except ValueError:
        pass
    return pick
