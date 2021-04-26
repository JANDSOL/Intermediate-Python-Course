def palindrome(string):
    """Try, except and rise"""
    try:
        if len(string) == 0:
            raise ValueError('No se puede ingresar una cadena vacía.')
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


if __name__ == '__main__':
    try:
        print(palindrome(''))
        print('Fin del programa.')
    except TypeError:
        print('Solo puede ingresar strings.')
