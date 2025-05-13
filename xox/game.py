from xox.exceptions import Over, Win, Lose, Draw
from xox.string import string
from xox.loop import loop
from xox.rand import rand


def game():
    def show(state):
        print(string(state) + "\n")

    def x(state):
        show(state)
        return int(input("Your move: ")) - 1

    def o(state):
        show(state)
        return rand(state)

    try:
        loop(x, o)
    except Over as e:
        (state,) = e.args
        show(state)
        if isinstance(e, Win):
            print("You win!")
        elif isinstance(e, Lose):
            print("You lose!")
        elif isinstance(e, Draw):
            print("Draw!")
