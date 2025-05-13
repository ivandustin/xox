from numpy import array
from xox.exceptions import Win, Lose, Draw
from xox.is_draw import is_draw
from xox.is_win import is_win
from xox import X


def check(state: array, piece: int) -> None:
    if is_win(state, piece):
        if piece == X:
            raise Win(state)
        else:
            raise Lose(state)
    if is_draw(state):
        raise Draw(state)
