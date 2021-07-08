def my_func (num1, num2, num3):
    """
    Возвращает сумму наибольших двух аргументов.
    """
    ordered_numbers = sorted([num1, num2, num3])
    return ordered_numbers[1] + ordered_numbers[2]
print(my_func(-2, 16, -3))
