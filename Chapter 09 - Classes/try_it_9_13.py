import random


class Die:
    """Representation of a dice"""

    def __init__(self):

        self.sides = 20

    def describe_sides(self):
        """Tells a user how many sides the dice has."""
        print(f"This dice has {self.sides} sides.")

    def roll_dice(self):
        """Rolls a random number"""
        random_number = random.randint(1, 20)
        print(f"You rolled a {random_number}.")


my_dice = Die()
my_dice.describe_sides()
my_dice.roll_dice()
