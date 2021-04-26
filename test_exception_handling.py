def divisors(num):
    """Challenge"""
    """Use try, except and raise to raise an error if the 
    user enters a negative number in our divisor program"""
    try:
        if num < 0:
            raise ValueError('Solo puedes ingresar un número entero positivo.')
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)

def run():
    """Receive a number as a parameter and
    return a list with all its divisors"""
    try:
        num = int(input('Ingresa un número: '))
        print('\nDIVISORES DE', num)
        if divisors(num) != None:
            print(divisors(num))
        print('Termino el programa.')
    except ValueError:
        print('Debes ingresar un número.')


if __name__ == '__main__':
    run()
