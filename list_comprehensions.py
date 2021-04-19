def run():
    """Common list"""
    squares = []
    for number in range(1, 101):
        if number % 3 != 0:
            squares.append(number**2)


if __name__ == '__main__':
    run()