#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pprint import pprint
# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []
my_family.append('Отец')
my_family.append('Мать')
my_family.append('Младший брат Валера')
my_family.append('Средний брат Саша')
my_family.append('Старший брат Вася')
pprint(my_family)


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    [],
]
my_family_height[0] = ['Отец', 174]
my_family_height.append(['Мать', 165])
my_family_height.append(['Младший брат Валера', 173])
my_family_height.append(['Средний брат Саша', 183])
my_family_height.append(['Старший брат Вася', 179])


pprint(my_family_height)

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост', my_family_height[0][0], my_family_height[0][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print('Общий рост моей семьи -', my_family_height[0][1] + my_family_height[1][1]
      + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1], 'см')
