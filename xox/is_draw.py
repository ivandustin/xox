from numpy import array
from xox import EMPTY


def is_draw(state: array) -> bool:
    return all(state != EMPTY)
