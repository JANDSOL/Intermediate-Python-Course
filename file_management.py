def read():
    """Read files containing the numbers 1-10
    and convert each of their lines into lists"""
    with open("./archives/numbers.txt", 'r', encoding='UTF-8') as f:
        numbers = [int(line) for line in f]
        print(numbers)

def write():
    pass

def run():
    read()


if __name__ == '__main__':
    run()
