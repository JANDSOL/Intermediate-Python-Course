from math import sqrt as square_root

def run():
    """Common Dictionary"""
    my_dict = {}
    for num in range(1, 101):
        if num % 3 != 0:
            my_dict[num] = num**3
    print('***Lista Común***')
    print(my_dict)

    """Dictionary Comprehension"""
    my_dict_comp = {num: num**3 for num in range(1, 101) if num % 3 != 0}
    print('\n***Dictionary Comprehension***')
    print(my_dict_comp)

    """Common Dictionary Challenge"""
    my_dict2 = {}
    # I use round to limit the number of decimal places in
    # the root of the value.
    for num in range(1, 1001):
        my_dict2[num] = round(square_root(num), 3)
    print('\n***Diccionario Común del Reto***')
    print(my_dict2)


if __name__ == '__main__':
    run()
