from functools import reduce

def run():
    """Example Without Reduce"""
    my_list = [2, 2, 2, 2, 2]
    all_multiply = 1

    for number in my_list:
        all_multiply = all_multiply * number
    print('Ejemplo sin reduce:', all_multiply)

    """Example With Reduce"""
    all_multiply2 = reduce(lambda a, b: a * b, my_list)
    print('\nEjemplo con reduce:', all_multiply2)


if __name__ == '__main__':
    run()
