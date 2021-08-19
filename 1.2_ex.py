#Первый урок, вторая задача
time_sec = int(input("Время в секундах - "))
hours = time_sec // 3600
rem_sec = time_sec - 3600 * hours
minutes = rem_sec // 60
rem_sec2 = rem_sec - 60 * minutes
print(f"{hours:02}.{minutes:02}.{rem_sec2:02}")

