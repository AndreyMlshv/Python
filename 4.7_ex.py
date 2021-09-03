def fact_gen(a):
    s = 1
    for i in range(a, a + 1):
        s *= i
        yield s


a = 20
for index, el in enumerate(fact_gen(a)):
    print(f"#{index + 1} {el}")


















# from itertools import count
# from math import factorial
# def factgen():
#     for el in count(1):
#         yield factorial(el)
# gen = factgen()
# n = 0
# for elem in gen: #цикл выводит только первые 6 чисел
#     if n < 6:
#         print(elem)
#         n += 1
#     else:
#         break