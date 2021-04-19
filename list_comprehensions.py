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
    # my_list, multiple4, multiple6, multiple9 = [], [], [], []
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
        # multiple4.append(4 * number)
        # multiple6.append(6 * number)
        # multiple9.append(9 * number)
    # for i in multiple4:
    #     if i in multiple6 and i in multiple9:
    #         my_list.append(i)
    print('\n***Lista común del reto***')
    print(my_list)

    # """List Comprehension Challenge"""
    # multiple4, multiple6, multiple9 = \
    # [4 * number and 6 * number and 9 * number for number in range(1,101)]
    # my_list2 = [i for i  in multiple4 if i in multiple6 and i in multiple9]
    # print('\n***List comprehension del reto***')
    # print(my_list2)


if __name__ == '__main__':
    run()