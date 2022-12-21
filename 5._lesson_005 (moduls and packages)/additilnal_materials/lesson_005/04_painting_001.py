# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (Коты? Коровы? Люди? Трактор? Что придумается)

import simple_draw as sd
from functions_for_painting import draw_earth
from functions_for_painting import painting_rainbow
from functions_for_painting import draw_the_sun
from functions_for_painting import draw_the_tree
from functions_for_painting import draw_the_house

width_window = 1200
height_window = 800

sd.resolution = (width_window, height_window)
sd.background_color = (102, 205, 170)

height_earth = height_window/10
draw_earth.draw_the_earth(width=width_window, length=height_earth)  # Рисует землю
painting_rainbow.painting_rainbow(y=-200, radius=1200, step=8)  # Рисует радугу
draw_the_sun.draw_the_sun(y=700, beam=100)  # Рисует солнце

# Точки для отрисовки деревьев
point_tree_1 = sd.get_point(x=width_window/3*2, y=height_earth)
point_tree_2 = sd.get_point(x=width_window/5*4, y=height_earth+25)
point_tree_3 = sd.get_point(x=width_window-100, y=height_earth+35)
# Рисуем деревья
draw_the_tree.draw_tree(start_point=point_tree_1, length_branch=80, width=6)
draw_the_tree.draw_tree(start_point=point_tree_2, length_branch=45, width=4)
draw_the_tree.draw_tree(start_point=point_tree_3, length_branch=40, width=4)

# Нижняя левая точка для отрисовки дома
point_left_lower_corner_house = sd.get_point(300, height_earth)
# Строим ДОМ
draw_the_house.draw_the_house(start_point=point_left_lower_corner_house,
                         quantity_bricks=15,
                         width_wall=300,
                         height_wall=300)



sd.pause()
