# 4-Напишите программу, которая по заданному номеру четверти,
#  показывает диапазон возможных координат точек в этой четверти (x и y)

quarter = int(input('Введите номер четверти (от 1 до 4) - '))
if quarter < 1 or quarter > 4:
    print('Не верное число повторите еще раз (циферки нужно от 1 до 4)')
elif quarter == 1:
    print('x > 0 и y > 0')
elif quarter == 2:
    print('x < 0 и y > 0')
elif quarter == 3:
    print('x < 0 и y < 0')
elif quarter == 4:
    print('x > 0 и y < 0')
