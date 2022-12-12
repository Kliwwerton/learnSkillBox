# -*- coding: utf-8 -*-
import simple_draw as sd
sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_DARK_ORANGE
# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
value = None
colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN,
          sd.COLOR_BLUE, sd.COLOR_PURPLE, sd.COLOR_WHITE)
color = colors[7]
while not isinstance(value, int):
    try:
        value = int(input('''Возможные цвета:
        0 - red
        1 - orange
        2 - yellow
        3 - green
        4 - cyan
        5 - blue
        6 - purple
        7 - ОСТАВИТЬ ПО УМОЛЧАНИЮ (БЕЛЫЙ)
        Выберите цвет: '''))
        if value < 0:
            print('Вы ввели слишком маленькое значение, попробуйте снова!')
            value = None
        elif 0 <= value < 8:
            color = colors[value]
        elif value > 7:
            print('Вы ввели слишком большое значение! Попробуйте снова.')
            value = None
    except ValueError:
        print("Вы ввели не число, пожалуйста введите число от 0 до 6")


def draw_the_figure(start_point, corner, number_of_corners, len_side, color, width=3):
    _value = 360 // number_of_corners
    start_point_2 = start_point
    corner_2 = corner
    while corner - corner_2 < 360 - _value:
        side = sd.get_vector(start_point=start_point, angle=corner, length=len_side, width=width)
        side.draw(color=color)
        start_point = side.end_point
        corner += _value
    sd.line(start_point=start_point, end_point=start_point_2, width=width, color=color)


def draw_for_the_people(point, corner, number_of_corners, len_side, color):
    draw_the_figure(start_point=point, corner=corner, number_of_corners=number_of_corners, len_side=len_side,
                    color=color)


point_0 = sd.get_point(900, 200)
point_1 = sd.get_point(300, 200)
point_2 = sd.get_point(300, 500)
point_3 = sd.get_point(900, 500)

draw_for_the_people(point=point_0, corner=10, number_of_corners=6, len_side=82, color=color)
draw_for_the_people(point=point_1, corner=40, number_of_corners=3, len_side=150, color=color)
draw_for_the_people(point=point_2, corner=60, number_of_corners=4, len_side=120, color=color)
draw_for_the_people(point=point_3, corner=30, number_of_corners=5, len_side=100, color=color)

sd.pause()
