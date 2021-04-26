def palindrome(string):
    """Try and except"""
    return string == string[::-1]


if __name__ == '__main__':
    try:
        print(palindrome(1))
    except TypeError:
        print('Solo puede ingresar strings.')
