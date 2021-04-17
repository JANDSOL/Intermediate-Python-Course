def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'firstname': 'Juan', 'lastname' : 'Andrade'}

    nested_list = [
        {'firstname': 'Juan', 'lastname' : 'Andrade'},
        {'years' : '19', 'actual state' : 'Single'},
        {'favorite food': 'Seafood', 'favorite drink' : 'Coca-Cola'},
        {"pet's name": 'kimba', 'favorite color': 'cold colors', },
    ]

    nested_dict = {
        'fruits': ['apple, grape, banana, pear'],
        'programming languages': ['python', 'java', 'c++', 'kotlin'],
        'names': ['Jhon', 'Peter', 'Kike'],
    }

    for idx in nested_list:
        for key, value in idx.items():
            print(key + ':', value)
    
    print('')

    for key, value in nested_dict.items():
            print(key + ':', value)


if __name__ == '__main__':
    run()
