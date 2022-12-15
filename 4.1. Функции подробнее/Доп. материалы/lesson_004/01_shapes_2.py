# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_DARK_CYAN

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   — копипастим её, меняем название, чуть подправляем код,
#   — копипастим её, меняем название, чуть подправляем код,
#   — и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg


def draw_polygon(start_point=sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2),
                 corners=4,
                 angle=0, length_side=100, color=sd.COLOR_WHITE, width=2):
    alpha = 360 / corners
    betta = start_point
    for i in range(corners - 1):
        start_point = sd.vector(start=start_point, angle=angle, length=length_side, color=color, width=width)
        angle += alpha
    sd.line(start_point=start_point, end_point=betta, color=color, width=width)


def draw_triangle(start_point, corner=30, length_side=150):
    side = sd.vector(start=start_point, angle=corner, length=length_side, width=2)
    corner += 360/3
    side_2 = sd.vector(start=side, angle=corner, length=length_side, width=2)
    corner += 360/3
    sd.vector(start=side_2, angle=corner, length=length_side, width=2)


def draw_square(start_point, corner=30, length_side=150):
    side = sd.vector(start=start_point, angle=corner, length=length_side, width=2)
    corner += 360/4
    side_2 = sd.vector(start=side, angle=corner, length=length_side, width=2)
    corner += 360/4
    side_3 = sd.vector(start=side_2, angle=corner, length=length_side, width=2)
    corner += 360 / 4
    sd.vector(start=side_3, angle=corner, length=length_side, width=2)


def draw_pentagon(start_point, corner=30, length_side=150):
    side = sd.vector(start=start_point, angle=corner, length=length_side, color=sd.COLOR_DARK_RED, width=2)
    corner += 360 / 5
    side_2 = sd.vector(start=side, angle=corner, length=length_side, color=sd.COLOR_DARK_RED, width=2)
    corner += 360 / 5
    side_3 = sd.vector(start=side_2, angle=corner, length=length_side, color=sd.COLOR_DARK_RED, width=2)
    corner += 360 / 5
    side_4 = sd.vector(start=side_3, angle=corner, length=length_side, color=sd.COLOR_DARK_RED, width=2)
    corner += 360 / 5
    sd.line(start_point=side_4, end_point=start_point, color=sd.COLOR_DARK_RED, width=2)


def draw_hexagon(start_point, corner=30, length_side=150, color=sd.COLOR_DARK_ORANGE, width=2):
    side = sd.vector(start=start_point, angle=corner, length=length_side, color=color, width=width)
    corner += 360 / 6
    side_2 = sd.vector(start=side, angle=corner, length=length_side, color=color, width=width)
    corner += 360 / 6
    side_3 = sd.vector(start=side_2, angle=corner, length=length_side, color=color, width=width)
    corner += 360 / 6
    side_4 = sd.vector(start=side_3, angle=corner, length=length_side, color=color, width=width)
    corner += 360 / 6
    side_5 = sd.vector(start=side_4, angle=corner, length=length_side, color=color, width=width)
    sd.line(start_point=side_5, end_point=start_point, color=color, width=width)


point_0 = sd.get_point(300, 150)
point_1 = sd.get_point(900, 150)
point_2 = sd.get_point(300, 450)
point_3 = sd.get_point(900, 450)
point_4 = sd.get_point(600, 250)

# draw_triangle(start_point=point_0, corner=30)
# draw_pentagon(start_point=point_1, corner=10)
# draw_square(start_point=point_2, corner=30)
# draw_hexagon(start_point=point_3, corner=30, length_side=100, color=sd.COLOR_DARK_ORANGE)

# draw_polygon(start_point=point_4, corners=10, length_side=150)

draw_polygon(start_point=point_0, corners=3, angle=25, length_side=200, color=sd.COLOR_RED)
draw_polygon(start_point=point_1, corners=4, angle=25, length_side=200, color=sd.COLOR_RED)
draw_polygon(start_point=point_2, corners=5, angle=25, length_side=200, color=sd.COLOR_RED)
draw_polygon(start_point=point_3, corners=7, angle=25, length_side=150, color=sd.COLOR_RED)
draw_polygon(start_point=point_4, corners=5)


# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризованную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   — все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудьте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечных точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы, чтобы внести изменения в код? Выгода на лицо
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!

sd.pause()
