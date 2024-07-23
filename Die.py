from random import randint

class ADie:

    def __init__(self, sideCount = 6) -> None:
        self.noOfSides = sideCount

    def roll(self):
        return randint(1, self.noOfSides)