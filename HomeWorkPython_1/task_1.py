# 1- Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input('Введите число от 1 до 7 - '))
if day < 1 or day > 7:
    print('Введено не корректное число, необходимо ввести от 1 до 7')
elif day == 6:
    print(f'{day} - ДА, это Cуббота')
elif day == 7:
    print(f'{day} - ДА, это Воскресенье')
else:
    print(f'{day} - НЕТ, ещё не выходной')   
  