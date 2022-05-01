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
all_songs: set = [] #  пишешь СЕТ, а задаешь ЛИСТ
all_songs_name: set = [] # создал, но не используешь, почему?

for x, y in violator_songs:
        if x == 'Halo' or x == 'Enjoy the Silence' or x == 'Clean': #вот тут имел в виду if x in {'Halo', "Enjoy the Silence", 'Clean'}
            all_songs.append(y)
count_songs = round(sum(all_songs), 2)

print(f'Три песни звучат {round(count_songs,2)} минут') # зачем второй раз раунд?



#  Наилучшим способом выполнить это задание, будет создать любой массив с нужными данными (set, tuple или list) в котором
#  будут названия нужных песен и проверять в условие наличие в виде ЕСЛИ песня В списке ТО
#  Итерируйся не по ренжу, а по списку песен (тоже самое, что писал в модуле с семьей) - понимаю как итерироваться, но тогда данные не получается правильно брать. 
# Создал массив уже с нужными суммами и сложил.



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

suma: float = on_track + to_the_sea + beyond_mirrors

print(f'А другие три песни звучат приблизительно {suma} минут') # тут всё ок,
# но лучше вынести сумму продолжительности треков в отдельную переменную


# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# ЗАЧЕТ