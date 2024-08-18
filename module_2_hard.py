import random

number_one = random.randint(8, 8)
print(f'Число из первой вставки {number_one}')
multiplier = []
list_result = []
for i in range(3, number_one // 2 + 1):  # поиск делителей числа
    if number_one % i == 0:
        multiplier.append(i)
multiplier.append(number_one)   # само число всегда делитель

for i in range(1, number_one // 2 + number_one % 2):
    for j in range(len(multiplier)):
        if i < multiplier[j] // 2 + multiplier[j] % 2:
            list_result.extend((i, multiplier[j] - i))

result = ''.join(list(map(str, list_result)))
print(f'Пароль для второй вставки {result}')
