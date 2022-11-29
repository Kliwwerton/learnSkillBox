#!/usr/bin/env python
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

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_quantity_0 = store[goods['Стол']][0]['quantity']
table_quantity_1 = store[goods['Стол']][1]['quantity']
table_total = table_quantity_0 + table_quantity_1
table_price_0 = store[goods['Стол']][0]['price']
table_price_1 = store[goods['Стол']][1]['price']

table_cost = table_quantity_0 * table_price_0 + table_quantity_1 * table_price_1
print('Стол -', table_total, 'шт, стоимость', table_cost, 'руб.')

couch_quantity_0 = store[goods['Диван']][0]['quantity']
couch_quantity_1 = store[goods['Диван']][1]['quantity']
couch_total = couch_quantity_0 + couch_quantity_1
couch_price_0 = store[goods['Диван']][0]['price']
couch_price_1 = store[goods['Диван']][1]['price']

couch_cost = couch_quantity_0 * couch_price_0 + couch_quantity_1 * couch_price_1
print('Диван -', couch_total, 'шт, стоимость', couch_cost, 'руб.')

chair_quantity_0 = store[goods['Стул']][0]['quantity']
chair_quantity_1 = store[goods['Стул']][1]['quantity']
chair_quantity_2 = store[goods['Стул']][2]['quantity']
chair_total = chair_quantity_0 + chair_quantity_1 + chair_quantity_2
chair_price_0 = store[goods['Стул']][0]['price']
chair_price_1 = store[goods['Стул']][1]['price']
chair_price_2 = store[goods['Стул']][2]['price']

chair_cost = chair_quantity_0 * chair_price_0 + chair_quantity_1 * chair_price_1 + chair_quantity_2 * chair_price_2
print('Стул -', chair_total, 'шт, стоимость', chair_cost, 'руб.')



# Вывести стоимость каждого товара на складе:
# один раз распечатать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################
