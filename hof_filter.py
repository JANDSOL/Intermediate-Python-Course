def run():
    """Example Without Filter"""
    my_list = [1, 4, 5, 6, 9, 13, 19, 21]
    odd_nums = [i for i in my_list if i % 2 != 0]
    print('***Números impares con List Comprehension***')
    print(odd_nums)

    """High Order Functions, Filter"""
    odd_nums2 = list(filter(lambda x: x % 2 != 0, my_list))
    print('\n***Números impares con Filter***')
    print(odd_nums2)


if __name__ == '__main__':
    run()
