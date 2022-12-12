# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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
        print("Вы ввели не число, пожалуйста введите число от 0 до 7")
number_of_corners = None
value_1 = None
while not isinstance(value_1, int):
    try:
        value_1 = int(input('''Возможные фигуры:
        0 - Треугольник
        1 - Квадрат
        2 - Пятиугольник (Пентагон)
        3 - Шестиугольник
        4 - Семиугольник
        5 - Восьмиугольник
               
        Выберите фигуру: '''))
        if value_1 < 0:
            print('Вы ввели слишком маленькое значение, попробуйте снова!')
            value_1 = None
        elif 0 <= value_1 <= 5:
            number_of_corners = value_1 + 3
        elif value_1 > 5:
            print('Вы ввели слишком большое значение! Попробуйте снова.')
            value_1 = None
    except ValueError:
        print("Вы ввели не число, пожалуйста введите число от 0 до 5")


def draw_the_figure(start_point, corner, _number_of_corners, len_side, color, width=3):
    ''' Рисует фигуру с заданными параметрами:
    начальная точка, угол наклона первого вектора, число углов - не ограничено, длина вектора,
     цвет векторов, толщина линий
    '''
    _value = (360 // _number_of_corners)
    start_point_2 = start_point
    corner_2 = corner
    while corner - corner_2 < 360 - _value:
        side = sd.get_vector(start_point=start_point, angle=corner, length=len_side, width=width)
        side.draw(color=color)
        start_point = side.end_point
        corner += _value
    sd.line(start_point=start_point, end_point=start_point_2, width=width, color=color)


point_0 = sd.get_point(600, 300)
point_1 = sd.get_point(300, 200)
point_2 = sd.get_point(300, 500)
point_3 = sd.get_point(900, 500)

draw_the_figure(start_point=point_0, corner=10, _number_of_corners=number_of_corners, len_side=100, color=color)

sd.pause()
