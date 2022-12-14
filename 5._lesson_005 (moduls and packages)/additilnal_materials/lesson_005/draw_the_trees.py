# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = (30, 144, 255)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомно отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомно отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


def draw_bunches(start_point, angle, length):
    """Рисует дерево начиная с заданной точки, первая ветка под углом angle длиной length"""

    if length < 5:
        return
    color = (139, 69, 19)
    if length < 10:
        color = sd.COLOR_GREEN
    line = sd.get_vector(start_point=start_point, angle=angle, length=length, width=2)
    line.draw(color=color)
    start_point = line.end_point
    angle_1 = angle + sd.random_number(10, 30)
    length_change = sd.random_number(-20, 20)/100
    draw_bunches(start_point=start_point, angle=angle_1, length=length*(0.75+length_change))
    angle_2 = angle - sd.random_number(10, 30)
    draw_bunches(start_point=start_point, angle=angle_2, length=length*(0.75+length_change))
