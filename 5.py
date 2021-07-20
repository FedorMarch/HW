from functools import reduce

my_list = [el for el in range(100, 1001) if el % 2 == 0]
def multiply(el1, el2):
    return el1 * el2
print(reduce(multiply, my_list))
