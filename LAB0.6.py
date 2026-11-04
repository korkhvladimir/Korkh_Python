date_input = input("Введите дату рождения ")

day, month = map(int, date_input.split("."))

if (month == 3 and day >= 21) or (month == 4 and day <= 19): zodiac = "Овен" 
elif (month == 4 and day >= 20) or (month == 5 and day <= 20): zodiac = "Телец" 
elif (month == 5 and day >= 21) or (month == 6 and day <= 20): zodiac = "Близнецы" 
elif (month == 6 and day >= 21) or (month == 7 and day <= 22): zodiac = "Рак" 
elif (month == 7 and day >= 23) or (month == 8 and day <= 22): zodiac = "Лев" 
elif (month == 8 and day >= 23) or (month == 9 and day <= 22): zodiac = "Дева"
elif (month == 9 and day >= 23) or (month == 10 and day <= 22): zodiac = "Весы"
elif (month == 10 and day >= 23) or (month == 11 and day <= 21): zodiac = "Скорпион" 
elif (month == 11 and day >= 22) or (month == 12 and day <= 21): zodiac = "Стрелец"
elif (month == 12 and day >= 22) or (month == 1 and day <= 19): zodiac = "Козерог" 
elif (month == 1 and day >= 20) or (month == 2 and day <= 18): zodiac = "Водолей" 
else: zodiac = "Рыбы"
print(f"Вывод: {zodiac}")