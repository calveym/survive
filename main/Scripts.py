import datetime
import random
from main.Character import Player

"""
All game functions and logic

Takes input from player, processes input, updates gamestate and outputs
additional information.
"""
class Game:
    """
    Increases food randomly.

    Creates random number, uses input time in calculation of gathered food,
    updates inventory for food quantity.
    """
    def forage(self):
        chance = random.randint(0, 3)
        foodGathered = chance * self
        print(foodGathered, "food gathered.\n\n")
        Player.inventory['food'] += foodGathered

    def feed(self):
        return()

    def train(self):
        return()

    def build(self):
        return()

    def explore(self):
        return()

    def signal(self):
        return()

    def interact(self):
        return()

    def inventory(self):
        return()

    def intro(self):
        return()

    def story(self):
        return()

    def escape(self):
        return ()

    def failure(self):
        return ()

    def play(self):
        return()