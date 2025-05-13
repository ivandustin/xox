from numpy import array, all
from .indices import INDICES


def is_win(state: array, piece: int) -> bool:
    for index in INDICES:
        if all(state[index] == piece):
            return True
    return False
