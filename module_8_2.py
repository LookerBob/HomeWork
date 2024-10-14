def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    i = 0
    try:
        for num in numbers:
            if not isinstance(num, int):
                print(f'Некорректный тип данных для подсчёта суммы - {num}')
            else:
                i += 1
        return personal_sum(numbers)[0] / i
    except TypeError:
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0


# print(personal_sum((0,1,1,1,'s',1,2)))

print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать