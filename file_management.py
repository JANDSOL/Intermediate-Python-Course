def read():
    """Read files containing the numbers 1-10
    and convert each of their lines into lists"""
    with open("./archives/numbers.txt", 'r', encoding="UTF-8") as f:
        numbers = [int(line) for line in f]
        print(numbers)

def write():
    """Save names from a list to a file"""
    names = ['Juan', 'Pablo', 'Pedro', 'Jesús', 'María']
    names2 = ['Fernanda', 'Lola', 'Esperanza', 'Esther', 'Lucas']
    with open("./archives/names.txt", "a", encoding="UTF-8") as f:
        for name in names2:
            f.write(name)
            f.write('\n')

def run():
    write()


if __name__ == '__main__':
    run()
