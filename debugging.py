def divisors(num):
    """Receive a number as a parameter and
    return a list with all its divisors"""
    divisors = [i for i in range(1, num + 1) if num % i == 1]
    return divisors

def run():
    num = int(input('Ingresa un número: '))
    print('\nDIVISORES DE', num)
    print(divisors(num))


if __name__ == '__main__':
    run()