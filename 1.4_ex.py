#Превый урок, четвертое задание
us_numb = int(input("Введите целое, положительное число:"))
check_var = -1
while us_numb > 10:
    rem = us_numb % 10
    us_numb //= 10
    if rem > check_var:
        check_var = rem
print(check_var)

