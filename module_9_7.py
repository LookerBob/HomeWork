def is_prime(func):
    def wrapper(*args):
        x = func(*args)
        for i in range(2, (x // 2) + 1):
            if x % i == 0:
                print('Составное')
                return x
        print('Простое')
        return x

    return wrapper


@is_prime
def sum_three(*args):
    summa = 0
    for arg in args:
        summa += arg
    return summa


result = sum_three(2, 3, 6)
print(result)
