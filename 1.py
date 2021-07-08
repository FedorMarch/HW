num1 = int(input('Введите делимое'))
num2 = int(input('Введите делитель'))
def divide(num1, num2):
    if num2 == 0:
        return 'Ошибка: на ноль делить нельзя'
    return f'Результатом деления {num1} на {num2} является {num1 / num2}'
print(divide(num1, num2))
