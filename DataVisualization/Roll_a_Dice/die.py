from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, side_num = 6):
        self.side_num = side_num

    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.side_num)