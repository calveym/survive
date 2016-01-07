import datetime
import time
import random
from main.Character import Player

"""
All game functions and logic

Takes input from player, processes input, updates gamestate and outputs
additional information.
"""
class Game:

    class Survival:

        def forage(self):
            """
            Increases food randomly.

            Creates random number, uses input time in calculation of gathered food,
            updates inventory for food quantity. Adds small delay for user to wait.
            foodGathered = total food added to player
            """
            print("\n\nForaging for food...\n")
            chance = random.randint(0, 3)
            foodGathered = chance * self
            time.sleep(1)
            print(".\n")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print("\n\n" + str(foodGathered) + " food gathered.\n")
            time.sleep(1)
            str(input("[Hit Enter]"))
            Player.inventory['food'] += foodGathered

        def feed(self):
            return()

        def drink(self):
            return()

        def fire(self):
            return()

    class Construction:

        def build(self):
            return ()

        def gather(self):
            return()

    class Action:

        def train(self):
            return()

        def explore(self):
            return()

        def signal(self):
            return()

        def interact(self):
            return()

    class Ui:

        def inventory(self):
            return()

    class Play:

        def intro(self):
            return ()

        def story(self):
            return ()

        def escape(self):
            return ()

        def failure(self):
            return ()