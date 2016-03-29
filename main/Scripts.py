import time
import random
from main.character import Player
import main

location = {'name': '', 'difficulty': 0}


def init():
    print("Load previous game?(yes/no)")
    if str(input()) == 'yes':
        print("Loading game...")
        main.curstate = main.savedstate
    else:
        main.curstate = main.character

class Survival:
    """TODO: add base logic"""

    def forage(self):
        """
        Increases food randomly.
        """
        Ui.addevent(self, 'You go out in search of food.')
        time.sleep(1)
        Ui.printui(self)
        Ui.addevent('.')
        time.sleep(1)
        chance = random.randint(0, 3) - (int(location['difficulty']))
        Ui.addevent('Success!')
    def eat(self):
        """

        """
        Ui.addevent(self, 'You eat a scrap of food.')
        time.sleep(1)
        Ui.printui(self)

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

    def upgrade(self):
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
    """
    Defines all user interactions. Frontend communicates with backend logic.

    Menu changes based on previous input, restarts at mainmenu.
    :func inventory: prints inventory on call
    """

    mainmenu = ['Survival', 'Action', 'Construction', 'Inventory', '?']
    inventorymenu = []
    survivalmenu = ['Forage for Food', 'Eat Some Food', 'Take a Drink', 'Light a Fire', 'Return to Main Menu']
    constructionmenu = ['Build', 'Gather', 'Upgrade', 'Return to Main Menu', '?']
    actionmenu = ['Train', 'Explore', 'Signal', 'Interact', 'Return to Main Menu']
    secretmenu = ['Secret', 'Secret', 'Secret', 'Secret', 'Secret']
    menu = mainmenu
    eventlog = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    def addevent(self, text):
        Ui.eventlog.insert(0, text)
        del Ui.eventlog[13]
        return()

    def inventory(self):
        return()

    def mainmenuinput(self, userinput):
        """

        :param userinput: input from printui
        :return:
        """
        try:
            if Ui.menu == Ui.mainmenu:
                if userinput == 1:
                    Ui.menu = Ui.survivalmenu
                elif userinput == 2:
                    Ui.menu = Ui.actionmenu
                elif userinput == 3:
                    Ui.menu = Ui.constructionmenu
                elif userinput == 4:
                    Ui.menu = Ui.inventorymenu
                elif userinput == 5:
                    Ui.menu = Ui.secretmenu
            elif Ui.menu == Ui.survivalmenu:
                if userinput == 1:
                    Survival.forage()
                elif userinput == 2:
                    Survival.eat()
                elif userinput == 3:
                    Survival.drink()
                elif userinput == 4:
                    Survival.fire()
                elif userinput == 5:
                    Ui.menu = Ui.mainmenu
            elif Ui.menu == Ui.actionmenu:
                if userinput == 1:
                    Action.train()
                elif userinput == 2:
                    Action.explore()
                elif userinput == 3:
                    Action.signal()
                elif userinput == 4:
                    Action.interact()
                elif userinput == 5:
                    Ui.menu = Ui.mainmenu
            elif Ui.menu == Ui.constructionmenu:
                if userinput == 1:
                    Construction.build()
                elif userinput == 2:
                    Construction.gather()
                elif userinput == 3:
                    Construction.upgrade()
                elif userinput == 4:
                    Ui.menu = Ui.mainmenu
                elif userinput == 5:
                    Ui.menu = Ui.secretmenu
            elif Ui.menu == Ui.inventorymenu:
                if userinput == 1:
                    pass
                elif userinput == 2:
                    pass
                elif userinput == 3:
                    pass
                elif userinput == 4:
                    pass
                elif userinput == 5:
                    pass
            elif Ui.menu == Ui.secretmenu:
                if userinput == 1:
                    pass
                elif userinput == 2:
                    pass
                elif userinput == 3:
                    pass
                elif userinput == 4:
                    pass
                elif userinput == 5:
                    pass
            return Ui.printui(self)
        except:
            pass


    def printui(self):
        """Prints out user interface, with all necessary information and interactions."""
        print("____________________________________________________________________________________________________"
              "___________________")
        print("|Location: ", location['name'].ljust(27), "|  Time : ", str(Time.time).ljust(15), "Health : ",
              str(Player.stats['health']).ljust(15), "Water : ", str(Player.inventory['water']).ljust(16), "|")
        print("|                                       |  Day  : ", str(Time.day).ljust(15), "Money  : ",
              str(Player.inventory['money']).ljust(15), "Food  : ", str(Player.inventory['food']).ljust(16), "|")
        print("|_______________________________________|_________________________________________________"
              "_____________________________|")
        print("| Event Log:                                                          |                      "
              "Menu:                     |")
        for item in Ui.menu:
            print("|                                                                     | ",
                  Ui.menu.index(item) + 1, ":", item.ljust(41), "|")
        for x in Ui.eventlog:
            print("| ", Ui.eventlog.index(x), ": ", x.ljust(61), "|                                                |")
        print("|_____________________________________________________________________|_____________________________"
              "___________________|\n|")
        userinput = int(input("|    User Input: "))
        Ui.mainmenuinput(self, userinput)


class Play(object):

    def __init__(self):
        self.setup()

    def setup(self):
        """Makes player adjust console size, to fit UI. """
        Player.stats['name'] = str(input("Type your name: "))
        print("\nYou will now need to adjust the console size to fit the game UI.\n"
              "Go into your IDLE settings and adjust the window size to 120x30.\nEnsure that the two rows"
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

    def changelocation(self, newloc):
        location = main.data.locations.newloc
        return location


class Time:
    """Contains all aspects of temporal travel

    :function timepass: progresses game time
    """
    time = 6
    day = 0

    def timepass(self, timespent):
        """
        Progresses game time.

        :param timespent: number of hours ('time') game progresses by
        """

        return()

    def daypass(self, daysspent):
        return()
