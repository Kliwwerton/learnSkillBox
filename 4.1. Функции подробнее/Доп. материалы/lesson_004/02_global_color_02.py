# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_DARK_CYAN

COLORS = (sd.COLOR_WHITE,
          sd.COLOR_BLACK,
          sd.COLOR_RED,
          sd.COLOR_ORANGE,
          sd.COLOR_YELLOW,
          sd.COLOR_GREEN,
          sd.COLOR_CYAN,
          sd.COLOR_BLUE,
          sd.COLOR_PURPLE)

# Добавить цвет в функции рисования геометрических фигур из упр lesson_004/01_shapes.py
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

def draw_polygon(start_point=sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2),
                 corners=4,
                 angle=0, length_side=100, color=sd.COLOR_WHITE, width=2):
    alpha = 360 / corners
    betta = start_point
    for i in range(corners - 1):
        start_point = sd.vector(start=start_point, angle=angle, length=length_side, color=color, width=width)
        angle += alpha
    sd.line(start_point=start_point, end_point=betta, color=color, width=width)


custom_color = None
while not isinstance(custom_color, int):

    input("Введите выбранный цвет: ")
    if not isinstance(custom_color, int):
        print('Вы ввели не число')








point_0 = sd.get_point(300, 100)
point_1 = sd.get_point(900, 100)
point_2 = sd.get_point(300, 450)
point_3 = sd.get_point(900, 450)
point_4 = sd.get_point(600, 350)

draw_polygon(start_point=point_0, corners=3, angle=25, length_side=200, color=sd.COLOR_RED)
draw_polygon(start_point=point_1, corners=4, angle=25, length_side=200, color=sd.COLOR_RED)
draw_polygon(start_point=point_2, corners=5, angle=25, length_side=200, color=sd.COLOR_RED)
draw_polygon(start_point=point_3, corners=7, angle=25, length_side=150, color=sd.COLOR_RED)
draw_polygon(start_point=point_4, corners=5)


sd.pause()
