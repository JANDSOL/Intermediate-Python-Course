DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    """List Comprehension"""
    # Contains the name of the python developers.
    all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
    for worker in all_python_devs:
        print('Python devs:', worker)
    print('')

    # Contains the name of the platzi workers.
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    for worker in all_platzi_workers:
        print('Platzi workers:', worker)
    print('')
    
    """High Order Functions"""
    # Contains the workers adults.
    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    adults = list(map(lambda worker: worker['name'], adults))
    for worker in all_platzi_workers:
        print('Workers adults:', worker)
    print('')

    # Contains the workers old.
    old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA))
    for dicts in old_people:
        print(dicts)


if __name__ == '__main__':
    run()
