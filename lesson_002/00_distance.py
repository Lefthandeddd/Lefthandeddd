
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

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
def your_function(current_city: str, research_city: str) -> float:
    return float

'''
for current_city in cities_list:
    тут нужно задать ключ в словаре distances
    for research_city in cities_list:
        if current_city != research_city:
            distances[current_city][research_city] = your_function(current_city, research_city) 
'''