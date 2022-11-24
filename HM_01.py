# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input('Введите число: '))
if number > 0 and number < 7:
    if number >= 1 or number <= 5:
        print('Это будний день')
    else:
        print('Этот день выходной')
else:
    print('Введите число обозначающее день недели')

# Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите координату Х: '))
y = int(input('Введите координату Y: '))
if x != 0 and y != 0:
    if x > 0 and y > 0:
        print('Первая четверть')
    elif x < 0 and y > 0:
        print('Вторая четверть')
    elif x < 0 and y < 0:
        print('Третья четверть')
    elif x > 0 and y < 0:
        print('Четвертая четверть')
else:
    print('Центр оси координат. Введите координаты не равные нулю')


# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


number = int(input('Введите четверть плоскости: '))
if number > 0 and number < 5:
    if number == 1:
        print('(+∞, +∞)')
    elif number == 2:
        print('(-∞, +∞)')
    elif number == 3:
        print('(-∞, -∞)')
    elif number == 4:
        print('(+∞, -∞)')
else:
    print('Введите число обозначающее плоскость')

# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
import math
point_a = (float(input('Введите координату X точки А: ')),
           float(input('Введите координату Y точки А: ')))
point_b = (float(input('Введите координату X точки B: ')),
           float(input('Введите координату Y точки B: ')))
print(f'A = {point_a}, B = {point_b}')

result = round(math.sqrt(((point_b[0] - point_a[0])**2) + ((point_b[1] - point_a[1])**2)), 3)
print('Расстояние между точками =', result)
