# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

x = 1200
y = 800

sd.background_color = sd.COLOR_BLACK
sd.resolution = (x, y)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

a, b, c = 50, 50, x - 100
for i in rainbow_colors * 30:
    point_start = sd.get_point(a, b)
    point_finish = sd.get_point(c, y - 50)
    step = 5
    sd.line(start_point=point_start, end_point=point_finish, color=i, width=4)
    a += step
    # b += step
    c += step / 12
    # d += step

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (см sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


# def bubble(point, radius, color, width):
#     sd.circle(center_position=point, radius=radius, width=width, color=color)

point = sd.get_point(x - 300, y - 1100)
radius = 1050
for i in rainbow_colors:
    # color = i
    step2 = 20
    width = step2
    # bubble(point, radius, color, width)
    sd.circle(center_position=point, radius=radius, width=width, color=i)
    radius -= step2

sd.pause()
