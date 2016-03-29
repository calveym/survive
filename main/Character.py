class Player:
    """
    Defines all character related attributes. Used by scripts.py.
    """

    day = 0
    timeofday = 6
    stats = {
             'name': 'Player',
             'health': 100,
             'speed': 1,
             'intelligence': 1,
             'rads': 0,
    }

    inventory = {
                 'money': 0,
                 'food': 10,
                 'water': 10
    }

    skills = {}

    buildings = {'shelter': 0,
                 'shed': 0,
                 'corral': 0,
                 'workshop': 0,
                 'outpost': 0
    }
