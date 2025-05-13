from random import choice
from xox.init import init
from xox.put import put
from xox import X, O


def loop(x, o):
    state = init()
    piece = choice([X, O])
    while True:
        index = x(state) if piece == X else o(state)
        state = put(state, index, piece)
        piece = O if piece == X else X
