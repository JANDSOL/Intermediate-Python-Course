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
    # I take the Least Common Multiple of 4, 6 and 9 = 36
    my_list = []
    NUM_RANGE = range(1, 279)
    for number in NUM_RANGE:
        if (number * 36) % 36 == 0:
            my_list.append(number * 36)

    print('\n***Lista común del reto***')
    print(my_list)

    """List Comprehension Challenge"""
    my_list_comp = [i*36 for i in NUM_RANGE if i * 36 % 36 == 0]
    print('\n***List comprehension del reto***')
    print(my_list_comp)


if __name__ == '__main__':
    run()