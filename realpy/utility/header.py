import math, random
from typing import Union
from numpy import matrixlib

_bbbb = matrixlib.asmatrix([[1, 0], [0, 1]])
_cccc = matrixlib.asmatrix([[5, 4], [2, 9]])
_bbbb *= _cccc
print(_bbbb)

__all__ = [
    "sqr", "sign", "degtorad", "radtodeg", "irandom", "irandom_range", "bezier4", "choose",
    "distribute", "probability_test", "lengthdir_x", "lengthdir_y",
    "point_distance", "point_direction"
]


def sqr(v: float) -> float:
    return v * v


def sign(x: float) -> int:
    ret = 0
    if x > 0:
        ret = 1
    elif x < 0:
        ret = - 1
    return ret


def degtorad(degree: float) -> float:
    return math.radians(degree * math.pi / 180)


def radtodeg(radian: float) -> float:
    return math.degrees(radian)


def bezier4(t: float, x1, x2, x3, x4) -> float:
    factor = 1 - t

    return factor * (factor * (factor * x1 + t * x2)
                     + t * (factor * x2 + t * x3)) + t * (factor * (factor * x2 + t * x3) + t * (factor * x3 + t * x4))


def lengthdir_x(length: float, direction: float) -> float:
    return math.cos(degtorad(direction)) * length


def lengthdir_y(length: float, direction: float):
    return -math.sin(degtorad(direction)) * length


def point_distance(X1: float, Y1: float, X2: float, Y2: float) -> float:
    return math.dist([X1, Y1], [X2, Y2])


def point_direction(X1: float, Y1: float, X2: float, Y2: float) -> float:
    return radtodeg(math.atan2(Y2 - Y1, X1 - X2))


def irandom(n: Union[int, float]) -> int:
    return random.randint(0, int(n))


def irandom_range(n1: Union[int, float], n2: Union[int, float]) -> int:
    return random.randint(int(n1), int(n2))


def distribute(x1: float, x2: float, ratio: float) -> float:
    if irandom(100) <= ratio * 100:
        return x1
    else:
        return x2


def probability_test(max: Union[int, float]) -> bool:
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