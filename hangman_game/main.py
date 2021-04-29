from os import system as window_clear    # In charge of refreshing our screen
from time import sleep
from random import randrange
from name_of_game import NameOfGame
from levels import Levels
from images import Images
from game_over import GameOver


def name_game():
    """It will print the name of the game"""
    window_clear('cls')
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

def remove_accents(w_from_list, w_entered):
    w_from_list = w_from_list.lower().replace('á', 'a').replace('é', 'e')\
                   .replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    w_entered = w_entered.lower().replace('á', 'a').replace('é', 'e')\
                   .replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
    return w_from_list, w_entered

def list_random():
    """It will bring up random words without
    repetitions from the word list."""
    return WORDS[randrange(0, NUM_OF_WORDS_IN_LIST)]

def main():
    """Game Body"""
    name_game()
    k_playing = ''
    keep_playing = True
    string_entered = ''

    while (keep_playing == True):  # Loop to keep playing.
        word = list_random()

        for num_image, picture_level in enumerate(LEVEL):  # Level tour.

            while(True):  # Loop to stop at each level.
                if num_image < 6:
                    """Validate if invalid characters are entered"""
                    print(picture_level)
                    print(DOLL_PICTURE[num_image])
                    string_entered = input('Ingresa una letra o palabra: ')
                    string_entered = string_entered.replace(' ', '')
                    if string_entered.isalpha():
                        # Check if it's letter.
                        if len(string_entered) == 1:
                            formatted_word, formatted_string_ent = \
                                remove_accents(word, string_entered)
                            if formatted_string_ent in formatted_word:
                                pass
                            else:
                                break
                        else:  # Check if it's word.
                            pass
                    else:
                        print('\n¡Ingresa una letra o palabra VÁLIDA!')
                        print('Espera...')
                        sleep(2)
                        window_clear('cls')
                else:
                    break  # Break loop if it reaches level 6.
            window_clear('cls')
        
        while (True):
            print(GAME_OVER)
            print(DOLL_PICTURE[num_image + 1])
            # Ask if you want to continue playing.
            k_playing = input('\n¿QUIERES SEGUIR JUGANDO?\n')
            k_playing = k_playing.replace(' ', '')
            k_playing = k_playing.lower()
            k_playing = k_playing.replace('í', 'i')
            k_playing = k_playing.replace('ó', 'o')
            if k_playing.isalpha() and k_playing == 'si':
                window_clear('cls')
                break
            elif k_playing.isalpha() and k_playing == 'no':
                keep_playing = False
                window_clear('cls')
                break
            else:
                print('\n¡Ingrese una respuesta válida!')
                print('Espera...')
                sleep(2)
                window_clear('cls')
    print(GAME_OVER)
    print(DOLL_PICTURE[6])


if __name__ == '__main__':
    LEVEL = Levels().LEVELS
    DOLL_PICTURE = Images().IMAGES
    GAME_OVER = GameOver().GAME_OVER
    WORDS = list_words()
    NUM_OF_WORDS_IN_LIST = len(WORDS) - 1
    main()
