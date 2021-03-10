from typing import Union, _T

__all__ = [
    "sqr", "sign", "degtorad", "radtodeg", "irandom", "irandom_range", "bezier4", "choose",
    "distribute", "probability_test", "lengthdir_x", "lengthdir_y",
    "point_distance", "point_direction"
]


def sqr(v: float) -> float:
    ...


def sign(x: float) -> int:
    ...


def degtorad(degree: float) -> float:
    ...


def radtodeg(radian: float) -> float:
    ...


def bezier4(t, x1, x2, x3, x4) -> float:
    ...


def lengthdir_x(length: float, direction: float) -> float:
    ...


def lengthdir_y(length: float, direction: float) -> float:
    ...


def point_distance(X1: float, Y1: float, X2: float, Y2: float) -> float:
    ...


def point_direction(X1: float, Y1: float, X2: float, Y2: float) -> float:
    ...


def irandom(n: Union[int, float]) -> int:
    ...


def irandom_range(n1: Union[int, float], n2: Union[int, float]) -> int:
    ...


def distribute(x1: float, x2: float, ratio: float) -> float:
    ...


def probability_test(max: Union[int, float]) -> bool:
    ...


def choose(*args):
    ...
