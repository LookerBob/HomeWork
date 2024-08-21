def calculate_structure_sum(*args):
    summa = 0
    for arg in args:
        if isinstance(arg, int):
            summa += arg
        elif isinstance(arg, str):
            summa += len(arg)
        elif isinstance(arg, dict):
            for key, value in arg.items():
                summa += calculate_structure_sum(key)
                summa += calculate_structure_sum(value)
        elif isinstance(arg, list | tuple | set):
            for item in arg:
                summa += calculate_structure_sum(item)
    return summa


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
