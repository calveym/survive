import main.data
import random
default1 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default2 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default3 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default4 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default5 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default6 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default7 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default8 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default9 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default10 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default11 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default12 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default13 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default14 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
default15 = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
withtrees1 = []
withtrees2 = []
withtrees3 = []
withtrees4 = []
withtrees5 = []
withtrees6 = []
withtrees7 = []
withtrees8 = []
withtrees9 = []
withtrees10 = []
withtrees11 = []
withtrees12 = []
withtrees13 = []
withtrees14 = []
withtrees15 = []


def addtrees(location, line):
    totalchance = location['wood']
    for tile in default1:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees1.append('X')
        else: withtrees1.append('0')
    for tile in default2:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees2.append('X')
        else:
            withtrees2.append('0')
    for tile in default3:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees3.append('X')
        else:
            withtrees3.append('0')
    for tile in default4:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees4.append('X')
        else:
            withtrees4.append('0')
    for tile in default5:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees5.append('X')
        else:
            withtrees5.append('0')
    for tile in default6:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees6.append('X')
        else:
            withtrees6.append('0')
    for tile in default7:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees7.append('X')
        else:
            withtrees7.append('0')
    for tile in default8:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees8.append('X')
        else:
            withtrees8.append('0')
    for tile in default9:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees9.append('X')
        else:
            withtrees9.append('0')
    for tile in default10:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees10.append('X')
        else:
            withtrees10.append('0')
    for tile in default11:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees11.append('X')
        else:
            withtrees11.append('0')
    for tile in default12:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees12.append('X')
        else:
            withtrees12.append('0')
    for tile in default13:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees13.append('X')
        else:
            withtrees13.append('0')
    for tile in default14:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees14.append('X')
        else:
            withtrees14.append('0')
    for tile in default15:
        if random.randint(1, totalchance) > (totalchance / 2):
            withtrees15.append('X')
        else:
            withtrees15.append('0')


def addbuildings():
    pass


def addwater():
    pass


def addloot():
    pass


def addstoryitem():
    pass


addtrees(main.data.locations['Volga banks'], default1)
addtrees(main.data.locations['Volga banks'], default2)
addtrees(main.data.locations['Volga banks'], default3)
addtrees(main.data.locations['Volga banks'], default4)
addtrees(main.data.locations['Volga banks'], default5)
print(withtrees1)
