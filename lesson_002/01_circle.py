#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
from typing import Tuple

radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

pi: float = 3.1415926 # Давай сразу писать типы. Например pi: float = 3.1415926
square = pi * radius ** 2 # для чего флоат, если ты и так задал pi как флоат?
print(round(square, 4)) # принято писать без пробела, если ты ставишь скобки

# TODO старайся не городить код, вычисли площадь в отдельной переменной, а потом округли переменную, код будет более читаемый
# Поправил выше, спс. 

# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
point_0 = (0, 0)
print(f'{bool(radius >= ((point_1[1] ** 2) + (point_1[0] ** 2)) ** 0.5)}')

# Аналогично для другой точки
point_2 = (90, 90)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
print(f'{bool(radius >= ((point_2[1] ** 2) + (point_2[0] ** 2)) ** 0.5)}')

# TODO Стирай за собой выполненные TODO
# TODO опять жоска городишь код. Если сможешь написать функцию, которая просто будет принимать точку, вычислять расстояние
#  и принтить правильный ответ - будет здорово
# Ниже что получилось. Tuple[int] ты написал, чтобы было понятно, какого типа данные заходят?
def check_point_inside_circle(point: Tuple[int]) -> bool:
    long: float = ((point[1] ** 2) + (point[0] ** 2)) ** 0.5
    return round(long, 1)

print(check_point_inside_circle(point_1))
print(check_point_inside_circle(point_2))
# если возращать бул, как ты написал, то возвращалось: <class 'bool'>
# Пример вывода на консоль:
#
# 77777.7777
# False
# False
