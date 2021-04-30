class CharacterReplacement:
    """Display manager for character replacement"""

    def __init__(self, word, formatted_word, string_entered, \
                 formatted_string_ent, found_letters):
        
        # Check if it's letter.
        if len(string_entered) == 1 or len(string_entered) == 0:
            if formatted_string_ent in formatted_word:
                index = 0
                for letter in formatted_word:
                    # Create dictionary with found letters.
                    if formatted_string_ent == letter:
                        found_letters[index] = letter
                    index += 1
                self.sorted_dashboard(found_letters, formatted_word, word)
            else:
                self.sorted_dashboard(found_letters, formatted_word, word)
        
        # Check if it's word.
        else:
            if formatted_string_ent == formatted_word:
                print('\n    ', end='')
                for letter in word:
                    print('  {}  '.format(letter), end='')
                print('\n    ' + ' --- ' * len(word))
            else:
                self.sorted_dashboard(found_letters, formatted_word, word)


    def sorted_dashboard(self, found_letters, formatted_word, word):
        squeletor = '\n    '
        for letter in formatted_word:
            # It will help us to know if the letter was found within the word.
            # and as a consequence, give a space only where it was not found.
            entered_bucle2 = False
            for key_value in found_letters.items():
                if key_value[1] == letter:
                    squeletor += ' {}  '.format(word[key_value[0]])
                    entered_bucle2 = True
                    break
            if entered_bucle2:
                continue
            else:
                squeletor += '    '
        print(squeletor)
        print('\n    ' + '--- ' * len(word))
