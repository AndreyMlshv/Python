words = input("Введите несколько слов, разделенных пробелом: ")
a = words.split(' ')
for i, el in enumerate(a, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{i}. - {el}")