def run():
    """Example Without Map"""
    my_list = [1, 2, 3, 4, 5]
    list_comp = [i**2 for i in my_list]
    print('***Cuadrados de los números con List C.***')
    print(list_comp)

    """Example With Map"""
    list_map = list(map(lambda x: x**2, my_list))
    print('\n***Cuadrados de los números con Map***')
    print(list_map)


if __name__ == '__main__':
    run()
