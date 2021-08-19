new_rate = int(input("Новый элемент рейтинга: "))
pre_list = [7, 5, 3, 3, 2]
c = pre_list.count(new_rate)
for element in pre_list:
    if c > 0:
        i = pre_list.index(new_rate)
        pre_list.insert(i+c, new_rate)
        break
    else:
        if new_rate > element:
            j = pre_list.index(element)
            pre_list.insert(j, new_rate)
            break
        elif new_rate < pre_list[len(pre_list) - 1]:
            pre_list.append(new_rate)
print(pre_list)