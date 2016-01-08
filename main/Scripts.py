import time
import random
from main.character import Player

gametime = {'time': 6, 'day': 0}

class Game:
    """
    All game functions and logic

    Takes input from player, processes input, updates gamestate and outputs
    additional information.
    """
    class Survival:

        def forage(self):
            """
            Increases food randomly.
            """

        def feed(self):
            """

            """
            return()

        def drink(self):
            return()

        def fire(self):
            return()

        def sleep(self):
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

        def printui(self):

            return()

    class Play:

        def setup(self):
            """Makes player adjust console size, to fit UI. """
            Player.stats['name'] = str(input("Type your name: "))
            print("\nYou will now need to adjust the console size to fit the game UI.\nPlease ensure that the two rows"
                  " of X's are visible, without space above or below them, and then hit [Enter].")
            print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
                  "\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27"
                  "\n28\n29\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            str(input())
            return()

        def intro(self):
            return ()

        def story(self):
            return ()

        def escape(self):
            return ()

        def failure(self):
            return ()

    def time(self, timespent):
        """
        Progresses game time.

        :param timespent: number of hours ('time') game progresses by
        """

        return()
