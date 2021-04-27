from os import system as window_clear    # In charge of refreshing our screen
from name_of_game import NameOfGame


def name_game():
    """It will print the name of the game"""
    NAME_OF_GAME = NameOfGame().NAME_GAME
    count = 0
    while(count < 21):
        for name in NAME_OF_GAME:
            print(name)
            window_clear('cls')
        count += 1

def main():
    name_game()


if __name__ == '__main__':
    main()
