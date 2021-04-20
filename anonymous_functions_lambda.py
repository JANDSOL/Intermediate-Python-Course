def palidrome(word):
    """One word palidrome without lambda"""
    if word == word[::-1]:
        return True
    else:
        return False


def run():
    """One word palindrome with lambda"""
    palindrome_lambda = lambda word: word == word[::-1]
    print('\nPalabra palíndroma con lambda:', palindrome_lambda('arenera'))


if __name__ == '__main__':
    print('Palabra palíndroma sin lambda:', palidrome('ana'))
    run()
