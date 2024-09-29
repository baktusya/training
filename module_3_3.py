def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

values_list = [5, 'блок', False]
values_list_2 = ['олово', 5.67 ]
values_dict = {'a': 56, 'b': 34.6, 'c': 'лось' }

print_params()
print_params(5, False, 'слово')
print_params('фонарь', 45.7)
print_params(b = 25)
print_params(c=[1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
