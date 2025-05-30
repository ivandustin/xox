from numpy import array, all
from xox.check import check
from xox import EMPTY


def put(state: array, index: int, piece: int) -> array:
    assert all(state[index] == EMPTY), state
    state[index] = piece
    check(state, piece)
    return state
