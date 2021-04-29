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
    words_already_chosen = []
    # Restart words without repetitions if all words were covered.
    if len(words_already_chosen) - 1 == NUM_OF_WORDS_IN_LIST:
        while(len(words_already_chosen) != 0):
            words_already_chosen.pop()
    # Check that there are no words that are repeated in the game.
    while(True):
        idx_list_random = randrange(0, NUM_OF_WORDS_IN_LIST + 1)
        if idx_list_random not in words_already_chosen:
            words_already_chosen.append(idx_list_random)
            break

    return WORDS[idx_list_random]

def ask_continue_playing(num_image, keep_playing, level_comp, counter_level_win):
    k_playing = ''
    while (True):
        if level_comp:
            print(GAME_OVER)
            print(DOLL_PICTURE[counter_level_win])
        else:
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

    return keep_playing

def main():
    """Game Body"""
    name_game()
    keep_playing = True
    string_entered = ''

    while (keep_playing == True):  # Loop to keep playing.
        level_complete = False
        lap_counter = 0
        word = list_random()

        for num_image, picture_level in enumerate(LEVEL):  # Level tour.

            while(level_complete == False):  # Loop to stop at each level.
                if num_image < 6:
                    """Validate if invalid characters are entered"""
                    print(picture_level)
                    print(DOLL_PICTURE[num_image])
                    string_entered = input('Ingresa una letra o palabra: ')
                    string_entered = string_entered.replace(' ', '')
                    if string_entered.isalpha():
                        FORMATTED_WORD, formatted_string_ent = \
                        remove_accents(word, string_entered)
                        print(FORMATTED_WORD)
                        input()
                        # Check if it's letter.
                        if len(string_entered) == 1:
                            if formatted_string_ent in FORMATTED_WORD:  
                                """TODO:
                                        1. Implementar un sistema de chequeo,
                                           para poder intercambiar los caracteres
                                           por los espacios vacios.
                                        2. Implementar otro módulo que juegue con esto
                                           del intercambio, investiga el .format() en
                                           strings.
                                        3. Condicional para que confirme si las letras
                                           completaron la palabra a buscar"""
                                window_clear('cls')
                            else:
                                lap_counter += 1
                                window_clear('cls')
                                break
                        else:  # Check if it's word.
                            if formatted_string_ent == FORMATTED_WORD:
                                level_complete = True
                                break
                            else:
                                lap_counter += 1
                                window_clear('cls')
                                break
                    else:
                        print('\n¡Ingresa una letra o palabra VÁLIDA!')
                        print('Espera...')
                        sleep(2)
                        window_clear('cls')
                else:
                    break  # Break loop if it reaches level 6.
            window_clear('cls')
        
        keep_playing = ask_continue_playing(num_image, keep_playing, \
                                            level_complete, lap_counter)
                                            
    if level_complete:
        print(GAME_OVER)
        print(DOLL_PICTURE[lap_counter])
    else:
        print(GAME_OVER)
        print(DOLL_PICTURE[6])


if __name__ == '__main__':
    LEVEL = Levels().LEVELS
    DOLL_PICTURE = Images().IMAGES
    GAME_OVER = GameOver().GAME_OVER
    WORDS = list_words()
    NUM_OF_WORDS_IN_LIST = len(WORDS) - 1
    main()
