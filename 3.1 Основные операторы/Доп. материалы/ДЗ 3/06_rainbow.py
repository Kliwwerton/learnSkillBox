# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.background_color = sd.COLOR_DARK_BLUE
sd.resolution = (1200, 800)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

a, b, c, d = 50, 50, 1100, 750
for i in rainbow_colors * 30:
    point_start = sd.get_point(a, b)
    point_finish = sd.get_point(c, d)
    step = 5
    sd.line(start_point=point_start, end_point=point_finish, color=i, width=4)
    a += step
    # b += step
    c += step/12
    # d += step

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (см sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


# def bubble(point, radius, color, width):
#     sd.circle(center_position=point, radius=radius, width=width, color=color)


x = 700
y = -300
point = sd.get_point(x, y)
radius = 1050
for i in rainbow_colors:
    # color = i
    step2 = 20
    width = step2
    # bubble(point, radius, color, width)
    sd.circle(center_position=point, radius=radius, width=width, color=i)
    radius -= step2

sd.pause()
