
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

from ast import Break


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}


distances = {'Moscow': {'London': round(((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2) ** 0.5, 2),
                        'Paris': round(((sites['Moscow'][0] - sites['Paris'][0]) ** 2 + (sites['Moscow'][1] - sites['Paris'][1]) ** 2) ** 0.5, 2),
                        },
             'London': {'Moscow': round(((sites['London'][0] - sites['Moscow'][0]) ** 2 + (sites['London'][1] - sites['Moscow'][1]) ** 2) ** 0.5, 2),
                        'Paris': round(((sites['London'][0] - sites['Paris'][0]) ** 2 + (sites['London'][1] - sites['Paris'][1]) ** 2) ** 0.5, 2),                   
                        },
             'Paris': {'Moscow': round(((sites['Paris'][0] - sites['Moscow'][0]) ** 2 + (sites['Paris'][1] - sites['Moscow'][1]) ** 2) ** 0.5, 2),
                       'London': round(((sites['Paris'][0] - sites['London'][0]) ** 2 + (sites['Paris'][1] - sites['London'][1]) ** 2) ** 0.5, 2),                                     
                       }
             }

print(distances)
#я минут 40 думал как циклами это все заполнить.. не понимаю как итерироваться по ключам словаря самостоятельно, типо словарь[1][0] Вот где 1 он ошибку выдает, если делать словарь[city][0] то норм.
# в текущем блоке заданий это необязательно, тут ты это делаешь для того чтобы понять как работают словари. ЗАЧЕТ

# можешь переделать ради интереса следующим образом:
# - функция возвращающая расстояние
# - задай список городов
# - проитерируйся по нему
# - внутри будет вложенная итерация по тому же списку, которая после проверки, что город не тот же самый, запустит для
# него функцию вычисления расстония.

# Подсказки:
# Итерироваться по словарю можно тремя способами:
# dict.keys() - возвращает ключи словаря
# dict.values() - возвращает значения словаря
# dict.items() - возвращает пару ключ-значение словаря (гугли если чё)

# функция вида (назови нормально потом):



#Сделал вариант с запросом к пользователю:
cities_list: list= list(sites.keys())

current_city: str = input(f'Введите город на выбор из списка {cities_list}, откуда стартуете: ')
while current_city not in cities_list:
    current_city: str = input(f'Вы ввели название города неверно. Пожалуйста, введите точное название из списка {cities_list}, откуда стартуете: ')

research_city: str = input(f'Введите город на выбор из списка {cities_list}, куда едете: ')
while research_city not in cities_list:
    research_city: str = input(f'Вы ввели название города неверно. Пожалуйста, введите точное название из списка {cities_list}, откуда стартуете: ')

answer: float = distances[current_city][research_city]
print(f'От {current_city} до {research_city} {answer} км')


#Второй вариант, где покажем все расстояния:
current_city: str = ''
research_city: str = ''


def dist_calculate(current_city: str, research_city: str) -> float:
    answer: float = distances[current_city][research_city]
    print(f'От {current_city} до {research_city} {answer} км')

for current_city in cities_list:
    for research_city in cities_list:
        if current_city != research_city:
            dist_calculate(current_city, research_city)

#Немного не понял твою задачу, ты хотел, чтобы я перезаполнил словарь с помощью этой функции или создал функцию, которая переберет весь словарь и красиво напечатает его?