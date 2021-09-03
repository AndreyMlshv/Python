from itertools import count, cycle


un_gen = count(3)
for i in un_gen:
    if i > 10:
        break
    print(i)

un_list = [1, 2, 6, 8]
un_gen_2 = cycle(un_list)
s = 0
for i in un_gen_2:
    if s > 20:
        break
    s += 1
    print(i)


