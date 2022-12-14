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


def draw_triangle(start_point, corner=30, length_side=150):
    side = sd.get_vector(start_point=start_point, angle=corner, length=length_side, width=2)
    side.draw(color=sd.COLOR_DARK_RED)
    start_point_side_2 = side.end_point
    corner += 360/3
    side_2 = sd.get_vector(start_point=start_point_side_2, angle=corner, length=length_side, width=2)
    side_2.draw(color=sd.COLOR_DARK_RED)
    start_point_side_3 = side_2.end_point
    corner += 360/3
    side_3 = sd.get_vector(start_point=start_point_side_3, angle=corner, length=length_side, width=2)
    side_3.draw(color=sd.COLOR_DARK_RED)


def draw_square(start_point, corner=30, length_side=150):
    side = sd.vector(start=start_point, angle=corner, length=length_side, width=2)
    start_point_side_2 = side
    corner += 360/4
    side_2 = sd.vector(start=start_point_side_2, angle=corner, length=length_side, width=2)
    start_point_side_3 = side_2
    corner += 360/4
    side_3 = sd.vector(start=start_point_side_3, angle=corner, length=length_side, width=2)
    start_point_side_4 = side_3
    corner += 360 / 4
    sd.vector(start=start_point_side_4, angle=corner, length=length_side, width=2)


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


point_0 = sd.get_point(300, 150)
draw_triangle(start_point=point_0, corner=30)
point_1 = sd.get_point(900, 150)
draw_pentagon(start_point=point_1, corner=10)
point_2 = sd.get_point(300, 450)
draw_square(start_point=point_2, corner=30)

sd.pause()
