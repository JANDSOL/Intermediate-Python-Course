from os import system as window_clear    # In charge of refreshing our screen
from name_of_game import NameOfGame
from levels import Levels
from images import Images


def name_game():
    """It will print the name of the game"""
    NAME_OF_GAME = NameOfGame().NAME_GAME
    count = 0
    while(count < 21):
        for name in NAME_OF_GAME:
            print(name)
            window_clear('cls')
        count += 1

def list_words():
    """Contains the list with words to guess"""
    with open('./archive/data.txt', 'r', encoding='UTF-8') as f:
        ls_words = [word.replace('\n', '') for word in f]
        return ls_words

def main():
    """Game Body"""
    name_game()


if __name__ == '__main__':
    LEVEL = Levels().LEVELS
    DOLL_PICTURE = Images().IMAGES
    WORDS = list_words()
    main()
