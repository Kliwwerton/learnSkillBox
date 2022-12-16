# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 800)

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,+


def draw_branch_1(start_point, length_branch, angle=90):

    """ Рисует основной ствол дерева и две ветки, исходящие от ствола. """

    trunk = sd.vector(start=start_point, angle=angle, length=length_branch, color=sd.COLOR_DARK_ORANGE, width=2)
    sd.vector(start=trunk, angle=angle + 30, length=length_branch * 0.75, color=sd.COLOR_DARK_ORANGE, width=2)
    sd.vector(start=trunk, angle=angle - 30, length=length_branch * 0.75, color=sd.COLOR_DARK_ORANGE, width=2)


point_0 = sd.get_point(600, 2)

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


def draw_branches_2(start_point, length_branch=150, corner=90, width=10):

    """Draws a tree with the same length of branch"""

    if length_branch > 5:
        branch = sd.vector(start=start_point, angle=corner, length=length_branch, width=width)
        length_branch *= 0.75
        draw_branches_2(start_point=branch, length_branch=length_branch, corner=corner + 30, width=width-1)
        draw_branches_2(start_point=branch, length_branch=length_branch, corner=corner - 30, width=width-1)

# 3) первоначальный вызов:
# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg
# можно поиграть - шрифтами - цветами и углами отклонения

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg


def draw_branches(start_point, length_branch=120, corner=90, width=10, color=sd.COLOR_DARK_ORANGE):

    """Draws a tree with random length of branch"""

    branch = sd.vector(start=start_point, angle=corner, length=length_branch, width=width, color=color)
    length_branch *= (0.75 + (random.randint(-10, 15)/100))
    alpha = corner + random.randint(-50, 0)
    betta = corner + random.randint(0, 50)
    if width > 2:
        width -= 2
    if length_branch < 7:
        color = sd.COLOR_GREEN
    if length_branch > 5:
        draw_branches(start_point=branch, length_branch=length_branch, corner=alpha, width=width, color=color)
        draw_branches(start_point=branch, length_branch=length_branch, corner=betta, width=width, color=color)


# Пригодятся функции


if __name__ == '__main__':
    # draw_branch_1(start_point=point_0, length_branch=200)  # Draws a tree with two branches
    # draw_branches_2(start_point=point_0, length_branch=200)  # Draws a tree with the same length of branch
    draw_branches(start_point=point_0,)  # Draws a tree with random length of branches

sd.pause()
