import numpy as np
import random

E = 1
X = 2
O = 3


class Win(Exception):
    pass


class Lose(Exception):
    pass


class Draw(Exception):
    pass


class XOX:
    def __init__(self):
        self.state = np.array([E] * 9)
        self.player = random.choice([X, O])
        self.update()

    def switch(self):
        self.player = X if self.player == O else O

    def update(self):
        if self.player == O:
            self.ai()

    def random(self):
        x = np.random.random(self.state.shape)
        x = np.where(self.state != 1, 0, x)
        return x.argmax() + 1

    def ai(self):
        self.move(self.random(), O)

    def check(self, player):
        if self.is_win(player):
            if player == X:
                raise Win()
            else:
                raise Lose()
        elif self.is_draw():
            raise Draw()

    def move(self, move, player=X):
        index = move - 1
        assert self.state[index] == E, "Invalid move"
        self.state[index] = player
        self.check(player)
        self.switch()
        self.update()

    def encode(self):
        return "".join(
            np.where(self.state == X, "x", np.where(self.state == O, "o", "."))
        )

    def show(self):
        s = self.encode()
        for i in range(0, len(s), 3):
            print(s[i : i + 3])

    def is_win(self, player):
        indices = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for index in indices:
            if np.all(self.state[index] == player):
                return True
        return False

    def is_draw(self):
        return np.all(self.state != 1)

    def start(self):
        while True:
            try:
                self.show()
                self.move(int(input("Enter your move: ")))
            except Win:
                self.show()
                print("You win!")
                break
            except Lose:
                self.show()
                print("You lose!")
                break
            except Draw:
                self.show()
                print("Draw!")
                break
