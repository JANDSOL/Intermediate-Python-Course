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

    """Challenge"""
    my_list, multiple4, multiple6, multiple9 = [], [], [], []
    for number in range(1, 2510):
        multiple4.append(4 * number)
        multiple6.append(6 * number)
        multiple9.append(9 * number)
    for i in multiple4:
        if i in multiple6 and i in multiple9:
            my_list.append(i)
    print('\n***Lista común del reto***')
    print(my_list)


if __name__ == '__main__':
    run()