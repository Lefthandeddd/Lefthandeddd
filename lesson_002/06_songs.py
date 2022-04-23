#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# Распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round
count_songs: float = 0

for song in range(len(violator_songs)):
    if violator_songs[song][0] == 'Halo' or 'Enjoy the Silence' or 'Clean':
        count_songs += violator_songs[song][1]

# TODO неправильно сделал. три песни не звучат 43.9 минут. Сложилась продолжительность всех песен из-за неправильного
#  условия. В чём косяк: твоё условие выглядит так ЕСЛИ название песни == "хало" ИЛИ "сайленс" ИЛИ "КЛИН"
#  чтобы это условие работало,
#  его нужно записать как ЕСЛИ название песни == "хало" ИЛИ название песни == "сайленс" ИЛИ название песни == "клин",
#  т.к. условие где написана просто строка будет False только тогда, когда строка пустая.
#  Другими словами написанное тобой условие всегда будет возвращать True.
#  Наилучшим способом выполнить это задание, будет создать любой массив с нужными данными (set, tuple или list) в котором
#  будут названия нужных песен и проверять в условие наличие в виде ЕСЛИ песня В списке ТО
#  Итерируйся не по ренжу, а по списку песен (тоже самое, что писал в модуле с семьей)

print(f'Три песни звучат {round(count_songs,2)} минут')


# Есть словарь песен группы Yellow со временем звучания с точностью до долей минут
pocket_universe_songs = {
    'Solar Driftwood': 1.85,
    'Celsius': 5.98,
    'More': 6.65,
    'On Track': 5.55,
    'Monolith': 6.35,
    'To the Sea': 5.77,
    'Magnetic': 5.88,
    'Liquid Mountain': 2.97,
    'Pan Blue': 5.52,
    'Resistor': 7.22,
    'Beyond Mirrors': 5.82,
}

# Распечатайте общее время звучания трех песен: 'On Track', 'To the Sea' и 'Beyond Mirrors'
#   А другие три песни звучат приблизительно ХХХ минут

on_track: float = pocket_universe_songs['On Track']
to_the_sea: float = pocket_universe_songs['To the Sea']
beyond_mirrors: float = pocket_universe_songs['Beyond Mirrors']

print(f'А другие три песни звучат приблизительно {on_track + to_the_sea + beyond_mirrors} минут') # тут всё ок,
# но лучше вынести сумму продолжительности треков в отдельную переменную


# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)