from random import randint


class Dice:
    def roll(self):
        x = randint(1, 6)
        y = randint(1, 6)
        return x, y


print(Dice().roll())
