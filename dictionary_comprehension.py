def run():
    """Common Dictionary"""
    my_dict = {}
    for num in range(1, 101):
        if num % 3 != 0:
            my_dict[num] = num**3
    print('***Lista Común***')
    print(my_dict)


if __name__ == '__main__':
    run()
