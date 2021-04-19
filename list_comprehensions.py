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

if __name__ == '__main__':
    run()