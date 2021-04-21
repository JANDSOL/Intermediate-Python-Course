def run():
    """Example Without Reduce"""
    my_list = [2, 2, 2, 2, 2]
    all_multiply = 1

    for number in my_list:
        all_multiply = all_multiply * number
    print('Ejemplo sin reduce:', all_multiply)


if __name__ == '__main__':
    run()
