import time
import random
import main
from main.character import Player
import main.savedstate
import main.locations

location = 'Concord'
difficulty = 2


class Survival:
    """TODO: add base logic"""

    @staticmethod
    def forage():
        """
        Increases food
        """
        ui.addevent('You go out in search of food.')
        time.sleep(1)
        ui.printui(False)
        ui.addevent('.')
        time.sleep(1)
        chance = random.randint(0, 5) - (int(difficulty))
        curstate.Player.inventory['food'] += chance
        ui.addevent('Success!' + str(chance) + 'food added!')

    @staticmethod
    def eat():
        """
        Reduces food by 1, replenishes 10 health.
        """
        ui.addevent('You eat a scrap of food.')
        curstate.Player.inventory['food'] -= 1
        time.sleep(1)
        ui.printui(True)

    @staticmethod
    def drink():
        """
        reduces water by 1, replenishes 5 health
        """

    @staticmethod
    def fire():
        return()

    @staticmethod
    def sleep():
        return()


class Construction:

    @staticmethod
    def build():
        return ()

    @staticmethod
    def gather():
        return()

    @staticmethod
    def upgrade():
        return()


class Action:

    @staticmethod
    def train():
        return()

    @staticmethod
    def explore():
        return()

    @staticmethod
    def signal():
        return()

    @staticmethod
    def interact():
        return()


class Ui:
    """
    Defines all user interactions. Frontend communicates with backend logic.

    Menu changes based on previous input, restarts at mainmenu.
    :func inventory: prints inventory on call

    """

    mainmenu = ['Survival', 'Action', 'Construction', 'Inventory', '?']
    inventorymenu = ['List Inventory', '', '', '', 'Return to Main Menu']
    survivalmenu = ['Forage for Food', 'Eat Some Food', 'Take a Drink', 'Light a Fire', 'Return to Main Menu']
    constructionmenu = ['Build', 'Gather', 'Upgrade', 'Return to Main Menu', '?']
    actionmenu = ['Train', 'Explore', 'Signal', 'Interact', 'Return to Main Menu']
    secretmenu = ['Secret', 'Secret', 'Secret', 'Secret', 'Return to Main Menu']
    menu = mainmenu
    eventlog = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    @staticmethod
    def addevent(text):
        ui.eventlog.insert(0, text)
        del ui.eventlog[13]
        return()

    @staticmethod
    def inventory():
        """Prints each inventory item to the eventlog.
        """
        for item in curstate.Player.inventory:
            ui.addevent(str(curstate.Player.inventory[item]).ljust(6) + " x " + item)
        ui.printui(True)

    @staticmethod
    def mainmenuinput(userinput):
        """

        :param userinput: input from printui
        :return:
        """
        try:
            if ui.menu == ui.mainmenu:
                if userinput == 1:
                    ui.menu = ui.survivalmenu
                elif userinput == 2:
                    ui.menu = ui.actionmenu
                elif userinput == 3:
                    ui.menu = ui.constructionmenu
                elif userinput == 4:
                    ui.menu = ui.inventorymenu
                elif userinput == 5:
                    ui.menu = ui.secretmenu
            elif ui.menu == ui.survivalmenu:
                if userinput == 1:
                    survival.forage()
                elif userinput == 2:
                    survival.eat()
                elif userinput == 3:
                    survival.drink()
                elif userinput == 4:
                    survival.fire()
                elif userinput == 5:
                    ui.menu = ui.mainmenu
            elif ui.menu == ui.actionmenu:
                if userinput == 1:
                    action.train()
                elif userinput == 2:
                    action.explore()
                elif userinput == 3:
                    action.signal()
                elif userinput == 4:
                    action.interact()
                elif userinput == 5:
                    ui.menu = ui.mainmenu
            elif ui.menu == ui.constructionmenu:
                if userinput == 1:
                    construction.build()
                elif userinput == 2:
                    construction.gather()
                elif userinput == 3:
                    construction.upgrade()
                elif userinput == 4:
                    ui.menu = ui.mainmenu
                elif userinput == 5:
                    ui.menu = ui.secretmenu
            elif ui.menu == ui.inventorymenu:
                if userinput == 1:
                    ui.inventory()
                elif userinput == 2:
                    construction.gather()
                elif userinput == 3:
                    construction.upgrade()
                elif userinput == 4:
                    ui.menu = ui.mainmenu
                elif userinput == 5:
                    ui.menu = ui.secretmenu
            elif ui.menu == ui.secretmenu:
                if userinput == 1:
                    pass
                elif userinput == 2:
                    pass
                elif userinput == 3:
                    pass
                elif userinput == 4:
                    pass
                elif userinput == 5:
                    ui.menu = ui.mainmenu
            return ui.printui(True)
        except ValueError:
            pass

    @staticmethod
    def printui(static):
        """Prints out user interface, with all necessary information and interactions.
        :param static: whether the interface allows user input. 0=no 1=yes
        """
        print("____________________________________________________________________________________________________"
              "___________________")
        print("|Location: ", location.ljust(27), "|  Time : ", str(curstate.Player.timeofday).ljust(15), "Health : ",
              str(curstate.Player.stats['health']).ljust(15), "Rads  : ", str(curstate.Player.stats['rads']).ljust(16),
              "|")
        print("|                                       |  Day  : ", str(curstate.Player.day).ljust(15),
              "Money  : ",
              str(curstate.Player.inventory['money']).ljust(15), "Food  : ",
              str(curstate.Player.inventory['food']).ljust(16), "|")
        print("|_______________________________________|_________________________________________________"
              "_____________________________|")
        print("| Event Log:                                                          |                      "
              "Menu:                     |")
        for item in ui.menu:
            print("|                                                                     | ",
                  ui.menu.index(item) + 1, ":", item.ljust(41), "|")
        for x in ui.eventlog:
            print("| ", ui.eventlog.index(x), ": ", x.ljust(61), "|                                                |")
        print("|_____________________________________________________________________|_____________________________"
              "___________________|\n|")

        def inputattempt():
            try:
                userinput = int(input())
                ui.mainmenuinput(userinput)
            except ValueError:
                ui.addevent("Invalid input! Please try again, enter a number in the menu.")
        if static is True:
            inputattempt()


class Play(object):

    def __init__(self):
        self.setup()

    @staticmethod
    def setup():
        """Makes player adjust console size, to fit UI. """
        Player.stats['name'] = str(input("Type your name: "))
        print("\nYou will now need to adjust the console size to fit the game UI.\n"
              "Go into your IDLE settings and adjust the window size to 120x30.\nEnsure that the two rows"
              " of X's are visible, without space above or below them, and then hit [Enter].")
        print("\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
              "\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15\n16\n17\n18\n19\n20\n21\n22\n23\n24\n25\n26\n27"
              "\n28\n29\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        str(input())

    @staticmethod
    def intro():
        return ()

    @staticmethod
    def story():
        return ()

    @staticmethod
    def escape():
        return ()

    @staticmethod
    def failure():
        return ()

    @staticmethod
    def changelocation(newloc):
        return


class Time:
    """Allows passage of time, as referenced through curstate.

    :function timepass: progresses game time by input
    :function daypass: progresses game day by input
    """

    @staticmethod
    def timepass(timespent):
        """
        Progresses game time. Runs game checks for every tick.
        Accesses curstate for current time.
        :param timespent: number of hours ('time') game progresses by
        """
        curstate.Player.timeofday += timespent
        return()

    @staticmethod
    def daypass(daysspent):
        curstate.Player.day += daysspent
        return()


print("Initialising...")
survival = Survival()
construction = Construction()
action = Action()
ui = Ui()
play = Play()
timeClass = Time()
print("Load previous game?(yes/no)")
if str(input()) == 'yes':
    print("Loading game...")
    curstate = main.savedstate
else:
    curstate = main.character
ui.printui(True)
