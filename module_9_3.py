first = ['Strings', 'Student', 'Computers', 'Test']
second = ['Строка', 'Урбан', 'Компьютер', 'Тестик']

first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))
second_result = ((len(first[x]) == len(second[x])) for x in range(len(first)))

print(list(first_result))
print(list(second_result))
