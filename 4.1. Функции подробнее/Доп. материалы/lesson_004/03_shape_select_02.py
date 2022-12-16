# -*- coding: utf-8 -*-

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# Нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_DARK_CYAN

COLORS = (
    sd.COLOR_WHITE,
    sd.COLOR_BLACK,
    sd.COLOR_RED,
    sd.COLOR_ORANGE,
    sd.COLOR_YELLOW,
    sd.COLOR_GREEN,
    sd.COLOR_CYAN,
    sd.COLOR_BLUE,
    sd.COLOR_PURPLE
    )


def draw_polygon(start_point=sd.get_point(sd.resolution[0]/2, sd.resolution[1]/2),
                 corners=4,
                 angle=0, length_side=100, _color=sd.COLOR_WHITE, width=2):
    alpha = 360 / corners
    betta = start_point
    for i in range(corners - 1):
        start_point = sd.vector(start=start_point, angle=angle, length=length_side, color=color, width=width)
        angle += alpha
    sd.line(start_point=start_point, end_point=betta, color=color, width=width)


custom_color = None

while not isinstance(custom_color, int):
    try:
        custom_color = int(input('''Возможные цвета:
        0 - white
        1 - black
        2 - red
        3 - orange
        4 - yellow
        5 - green
        6 - cyan
        7 - blue
        8 - purple
        Выберите цвет фигуры: '''))
        if custom_color < 0:
            print('Вы ввели слишком маленькое значение, попробуйте снова!')
            custom_color = None
        elif 0 <= custom_color <= 8:
            color = COLORS[custom_color]
            print('Вы выбрали цвет, теперь выберите фигуру.')
        elif custom_color > 8:
            print('Вы ввели слишком большое значение! Попробуйте снова.')
            custom_color = None
    except ValueError:
        print("Вы ввели не число, пожалуйста введите число от 0 до 8")

length_side_figure = 200
number_of_corners = None
custom_figure = None
while not isinstance(custom_figure, int):
    try:
        custom_figure = int(input('''Возможные фигуры:
        0 - Треугольник
        1 - Квадрат
        2 - Пятиугольник (Пентагон)
        3 - Шестиугольник
        4 - Ввести своё количество углов (не более 15)

        Выберите фигуру: '''))
        if custom_figure < 0:
            print('Вы ввели слишком маленькое значение, попробуйте снова!')
            custom_figure = None
        elif 0 <= custom_figure <= 3:
            number_of_corners = custom_figure + 3
        elif custom_figure == 4:
            print('Вы выбрали пункт "Ввести своё количество углов"\n')
            while not isinstance(number_of_corners, int):
                try:
                    number_of_corners = int(input('Выберите количество углов в фигуре (не более 15): '))
                    if number_of_corners < 3:
                        print('Вы ввели слишком маленькое значение, количество углов в фигуре не может быть меньше 3х!')
                        number_of_corners = None
                    elif 3 <= number_of_corners <= 15:
                        print(f'Вы выбрали {number_of_corners} углов, сейчас я нарисую такую фигуру...')
                        if number_of_corners > 9:
                            length_side_figure -= 80
                    elif number_of_corners > 15:
                        print('Вы ввели слишком большое значение!'
                              'Фигуры с количеством углов более 15 отображаются криво, '
                              'выберите пожалуйста значение от 3 до 15')
                        number_of_corners = None
                except ValueError:
                    print("Вы ввели не число, пожалуйста введите число от 0 до 5")
        elif custom_figure > 4:
            print('Вы ввели слишком большое значение! Попробуйте снова.')
            custom_figure = None
    except ValueError:
        print("Вы ввели не число, пожалуйста введите число от 0 до 4")


color_figure = COLORS[custom_color]
point_0 = sd.get_point(600, 200)

# point_1 = sd.get_point(900, 100)
# point_2 = sd.get_point(300, 450)
# point_3 = sd.get_point(900, 450)
# point_4 = sd.get_point(600, 350)

draw_polygon(start_point=point_0, corners=number_of_corners, angle=25,
             length_side=length_side_figure, _color=color_figure)
# draw_polygon(start_point=point_1, corners=4, angle=25, length_side=200, _color=color_figure)
# draw_polygon(start_point=point_2, corners=5, angle=25, length_side=200, _color=color_figure)
# draw_polygon(start_point=point_3, corners=7, angle=25, length_side=150, _color=color_figure)
# draw_polygon(start_point=point_4, corners=5, _color=color_figure)

sd.pause()
