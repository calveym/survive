from main.character import Player
from main.scripts import *
import setup
import main.savedstate


def main():
    """Main loop"""
    main.scripts.init()
    while True:
        setup.setup()


if __name__ == '__main__':
    main()
