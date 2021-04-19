def run():
    """Common list"""
    squares = []
    for number in range(1, 101):
        if number % 3 != 0:
            squares.append(number**2)

    """List comprehensions"""
    squ_with_com = [number**2 for number in range(1, 101) if number % 3 != 0]


if __name__ == '__main__':
    run()