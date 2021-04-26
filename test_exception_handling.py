def divisors(num):
    """Receive a number as a parameter and
    return a list with all its divisors"""    
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    try:
        num = int(input('Ingresa un número: '))
        print('\nDIVISORES DE', num)
        print(divisors(num))
        print('Termino el programa.')
    except ValueError:
        print('Debes ingresar un número.')


if __name__ == '__main__':
    run()
