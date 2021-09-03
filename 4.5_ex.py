from functools import reduce


def prod_nums(x, y):
    return x * y


a = [i for i in range(100, 1001, 2)]
print(reduce(prod_nums, a))



