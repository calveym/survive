import datetime
import random
from main.Character import Player


def forage():
    chance = random.randint(0, 3)
    food_old = Player.inventory['food']
    del Player.inventory['food']
    Player.inventory['Food'] = food_old + chance * Player.skills['Foraging']
    food_added = chance * Player.skills['Foraging']
    return(food_added)


def feed():
    return()


def train():
    return()


def build():
    return()


def explore():
    return()


def signal():
    return()


def interact():
    return()


def inventory():
    return()


def intro():
    return()


def story():
    return()


def escape():
    return ()


def failure():
    return ()
