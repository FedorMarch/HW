def my_func(x, y):
    result = 1
    for _ in range (1, abs(y - 1), 1):
        result = result / x
    return result
arg = int(input('Введите целый положительный аргумент степени'))
exp = int(input('Введите целый отрицательный показатель степени'))
print(my_func(arg, exp))
