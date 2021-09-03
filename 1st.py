#Первый урок, пятая задача
revenue=int(input("Выручка вашей фирмы: "))
costs=int(input("Издержки: "))
if revenue > costs:
    print("Ваша фирма работает с прибылью! Так держать")
    profit=revenue / costs
    print("Рентабельность выручки: ", profit)
    margin=revenue - costs
    workers=int(input("Cколько сотрудников в вашей фирме?"))
    profit_by_worker=margin / workers
    print("Прибыль генерируемая каждым сотрудником: ", profit_by_worker)
else:
    print("Фирма работает в минус")










