# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите число = ')
suma = 0
for item in number:
    if item.isdigit():
        # print(item)
        suma += int(item)
print(suma)    
