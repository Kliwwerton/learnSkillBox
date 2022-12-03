# -*- coding: utf-8 -*-
import random as rd

import simple_draw as sd

sd.resolution = (1600, 900)


# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей


def babble(center_babble, radius_babble=50, line_width=1):
    for _ in range(3):
        radius_babble += rd.randint(0, 30)
        sd.circle(center_position=center_babble, radius=radius_babble, width=line_width)


# Нарисовать 10 пузырьков в ряд
# for _ in range(10):
#     point = sd.get_point(x, y)
#     babble(center_babble=point, width_babble=2)
#     x += 100

# Нарисовать три ряда по 10 пузырьков
# for x in range(100, 1501, 150):
#     for y in range(100, 451, 150):
#         point = sd.get_point(x, y)
#         step = 10
#         radius = 50
#         thickness = rd.randint(1, 5)
#         babble(center_babble=point, radius_babble=radius, line_width=thickness)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами


for _ in range(100):
    x = rd.randint(70, 1530)
    y = rd.randint(70, 830)
    point = sd.get_point(x, y)
    radius, thickness = rd.randint(30, 70), rd.randint(1, 4)
    babble(point, radius_babble=radius, line_width=thickness)

sd.pause()
