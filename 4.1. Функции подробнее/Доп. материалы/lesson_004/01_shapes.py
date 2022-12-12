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
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def draw_triangle(point, corner, len_side, width=3):
#     side = sd.get_vector(start_point=point, angle=corner, length=len_side, width=width)
#     side.draw()
#     side_1 = sd.get_vector(start_point=side.end_point, angle=corner + 120, length=len_side, width=width)
#     side_1.draw(color=sd.COLOR_WHITE)
#     side_2 = sd.get_vector(start_point=side_1.end_point, angle=corner + 240, length=len_side, width=width)
#     side_2.draw(color=sd.COLOR_RED)
#
#
# def draw_square(point, corner, len_side, width=3):
#     side = sd.get_vector(start_point=point, angle=corner, length=len_side, width=width)
#     side.draw()
#     side_1 = sd.get_vector(start_point=side.end_point, angle=corner + 90, length=len_side, width=width)
#     side_1.draw(color=sd.COLOR_WHITE)
#     side_2 = sd.get_vector(start_point=side_1.end_point, angle=corner + 180, length=len_side, width=width)
#     side_2.draw(color=sd.COLOR_RED)
#     sd.line(start_point=side_2.end_point, end_point=point, width=width, color=sd.COLOR_GREEN)
#
#
# def draw_pentagon(point, corner, len_side, width=3):
#     side = sd.get_vector(start_point=point, angle=corner, length=len_side, width=width)
#     side.draw()
#     side_1 = sd.get_vector(start_point=side.end_point, angle=corner + 72, length=len_side, width=width)
#     side_1.draw(color=sd.COLOR_WHITE)
#     side_2 = sd.get_vector(start_point=side_1.end_point, angle=corner + 144, length=len_side, width=width)
#     side_2.draw(color=sd.COLOR_RED)
#     side_3 = sd.get_vector(start_point=side_2.end_point, angle=corner + 216, length=len_side, width=width)
#     side_3.draw(color=sd.COLOR_BLACK)
#     sd.line(start_point=side_3.end_point, end_point=point, width=width, color=sd.COLOR_GREEN)
#
#
# def draw_hexagon(point, corner, len_side, width=3):
#     side = sd.get_vector(start_point=point, angle=corner, length=len_side, width=width)
#     side.draw()
#     side_1 = sd.get_vector(start_point=side.end_point, angle=corner + 60, length=len_side, width=width)
#     side_1.draw(color=sd.COLOR_WHITE)
#     side_2 = sd.get_vector(start_point=side_1.end_point, angle=corner + 120, length=len_side, width=width)
#     side_2.draw(color=sd.COLOR_RED)
#     side_3 = sd.get_vector(start_point=side_2.end_point, angle=corner + 180, length=len_side, width=width)
#     side_3.draw(color=sd.COLOR_BLACK)
#     side_4 = sd.get_vector(start_point=side_3.end_point, angle=corner + 240, length=len_side, width=width)
#     side_4.draw(color=sd.COLOR_DARK_ORANGE)
#     sd.line(start_point=side_4.end_point, end_point=point, width=width, color=sd.COLOR_GREEN)


def draw_the_figure(start_point, corner, number_of_corners, len_side, color, width=3):
    value = 360 // number_of_corners
    start_point_2 = start_point
    corner_2 = corner
    while corner - corner_2 < 360 - value:
        side = sd.get_vector(start_point=start_point, angle=corner, length=len_side, width=width)
        side.draw(color=color)
        start_point = side.end_point
        corner += value
    sd.line(start_point=start_point, end_point=start_point_2, width=width, color=color)

    # side_1 = sd.get_vector(start_point=side.end_point, angle=corner + 120, length=len_side, width=width)
    # side_1.draw(color=sd.COLOR_WHITE)
    # side_2 = sd.get_vector(start_point=side_1.end_point, angle=corner + 240, length=len_side, width=width)
    # side_2.draw(color=sd.COLOR_RED)


point_0 = sd.get_point(900, 200)
point_1 = sd.get_point(300, 200)
point_2 = sd.get_point(300, 500)
point_3 = sd.get_point(900, 500)

# draw_triangle(point=point_0, corner=60, len_side=150)
# draw_square(point=point_1, corner=25, len_side=70)
# draw_pentagon(point=point_2, corner=36, len_side=120)
# draw_hexagon(point=point_3, corner=10, len_side=100)


def draw_for_the_people(point, corner, number_of_corners, len_side, color):
    draw_the_figure(start_point=point, corner=corner, number_of_corners=number_of_corners, len_side=len_side,
                    color=color)


draw_for_the_people(point=point_0, corner=25, number_of_corners=6, len_side=82, color=sd.COLOR_RED)
draw_for_the_people(point=point_1, corner=60, number_of_corners=3, len_side=150, color=sd.COLOR_RED)
draw_for_the_people(point=point_2, corner=25, number_of_corners=4, len_side=120, color=sd.COLOR_RED)
draw_for_the_people(point=point_3, corner=25, number_of_corners=5, len_side=90, color=sd.COLOR_RED)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
