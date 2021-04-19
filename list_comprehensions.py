def run():
    """Common list"""
    squares = []
    for number in range(1, 101):
        if number % 3 != 0:
            squares.append(number**2)
    print('***Lista Común***')
    print(squares)

    """List comprehension"""
    squ_with_com = [number**2 for number in range(1, 101) if number % 3 != 0]
    print('\n***List Comprehension***')
    print(squ_with_com)

    """Common List Challenge"""
    my_list = []
    multiple4, multiple6, multiple9 = 0, 0, 0
    NUM_RANGE = range(1, 2510)
    for multiple4 in NUM_RANGE:
        multiple4 = multiple4 * 4
        for multiple6 in NUM_RANGE:
            multiple6 = multiple6 * 6
            if multiple4 == multiple6:
                for multiple9 in NUM_RANGE:
                    multiple9 = multiple9 * 9
                    if multiple4 == multiple9:
                        my_list.append(multiple4)
    print('\n***Lista común del reto***')
    print(my_list)


if __name__ == '__main__':
    run()