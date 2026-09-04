my_dict = {
    'tuple': ('abc', 9, True, (2, 3), 'j'),
    'list': ['str', 5, 3.2, 3, '9.9'],
    'dict': {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5},
    'set': {8, 'm', 4.3, 2, 9}
}

my_dict['list'].append('new')
my_dict['list'].pop(2)
my_dict['dict']['i am a tuple'] = (888, 888, 888)
my_dict['dict'].pop('two')
my_dict['set'].add(777)
my_dict['set'].remove(8)
print(my_dict)
