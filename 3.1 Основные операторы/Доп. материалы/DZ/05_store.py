# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара на складе с помощью циклов.
# То есть: всего по лампам, стульям, етс.
# Формат строки вывода: "<товар> - <кол-во> шт, стоимость <общая стоимость> руб."
#
# Алгоритм должен получиться приблизительно такой:
#
# цикл for по товарам с получением кода и названия товара
#     инициализация переменных для подсчета количества и стоимости товара
#     получение списка на складе по коду товара
#     цикл for по списку на складе
#         подсчет количества товара
#         подсчет стоимости товара
#     вывод на консоль количества и стоимости товара на складе

# total_cost = 0
# for value in goods:
#     total = 0
#     cost = 0
#     # print(value)
#     # print(goods[value])
#     for k in store[goods[value]]:
#         total += k['quantity']
#         cost += total * k['price']
#
#     print(f'{value} - {total} штук, общая стоимость {cost} рублей.')
#     total_cost += cost
# print(f'Общая стоимость товаров на складе - {total_cost} рублей.')

total_cost = 0
for value in goods:
    code_value = goods[value]
    cost = 0
    quantity_value = 0
    for j in store[code_value]:
        quantity_value += j['quantity']
        cost += quantity_value * j['price']
        # print(cost)
    total_cost += cost
    print(f'Всего {value} на складе {quantity_value} на общую сумму {cost}')
