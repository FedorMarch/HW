sum = 0
number_check = True

while number_check:
    nums_to_sum = input('Введите числа, разделенные пробелом').split()
    for num in nums_to_sum:
        if num.isdigit():
            sum += int(num)
        else:
            print('Введен неверный символ')
            number_check = False
            break
    print(f'Сумма чисел, введенных за все время работы программы, равна {sum}')

