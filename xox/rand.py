from numpy.random import random
from numpy import array, where
from xox import EMPTY


def rand(state: array) -> int:
    return where(state == EMPTY, random(state.shape), 0).argmax()
