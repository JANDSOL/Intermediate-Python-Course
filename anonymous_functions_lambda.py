def palidrome(word):
    """One word palidrome without lambda"""
    if word == word[::-1]:
        return True
    else:
        return False
    

if __name__ == '__main__':
    print(palidrome('eana'))
