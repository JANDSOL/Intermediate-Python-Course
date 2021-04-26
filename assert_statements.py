def divisors(num):
    """Receive a number as a parameter and
    return a list with all its divisors"""
    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors

def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), 'Debes ingresar un número.'
    print('\nDIVISORES DE', num)
    print(divisors(int(num)))


if __name__ == '__main__':
    run()
