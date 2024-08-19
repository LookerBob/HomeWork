def print_params(a=1, b='строка', c=True):
  print(a, b, c)

print_params()
print_params(2)
print_params(1, 2, 4)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [500, 'мискузи', False]
values_dict = {'a': 250, 'b': 'массаракш', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2, 'туземун']
print_params(*values_list_2, 42)