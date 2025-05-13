from numpy import array, where
from xox import X, O


def string(state: array) -> str:
    x = state.reshape(3, 3)
    x = where(x == X, "x", where(x == O, "o", "."))
    return "\n".join("".join(row) for row in x)
