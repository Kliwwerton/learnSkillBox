# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random as rd
sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_DARK_BLUE

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.


def smiley_draw(point_x, point_y, color, width):

    """ Рисует круглый смайлик """

    point_center = sd.get_point(point_x, point_y)
    point_center_left_yae = sd.get_point(point_x - 20, point_y + 20)
    point_center_rihgt_yae = sd.get_point(point_x + 20, point_y + 20)
    sd.circle(point_center, radius=50, color=sd.random_color(), width=width)
    sd.circle(point_center, radius=5, color=sd.random_color(), width=width)
    sd.circle(point_center_left_yae, radius=5, color=color, width=width)
    sd.circle(point_center_rihgt_yae, radius=5, color=color, width=width)
    print(point_x, point_y)


def smiley_draw2(x, y, color, width=4):

    """Рисует восьмиугольный смайлик с глазами и носом"""

    point_center = sd.get_point(x, y) # Получение координат для центра смайлика
    points = [] # Список для храниения координат вершин многогранника
    # Координаты вершин многогранника (тела смайлика)
    point_a = sd.get_point(x - 30, y - 45)
    point_b = sd.get_point(x - 65, y - 15)
    point_c = sd.get_point(x - 65, y + 15)
    point_d = sd.get_point(x - 30, y + 45)
    point_e = sd.get_point(x + 30, y + 45)
    point_f = sd.get_point(x + 65, y + 15)
    point_g = sd.get_point(x + 65, y - 15)
    point_h = sd.get_point(x + 30, y - 45)
    # Добавление координат вершин в список
    points.append(point_a)
    points.append(point_b)
    points.append(point_c)
    points.append(point_d)
    points.append(point_e)
    points.append(point_f)
    points.append(point_g)
    points.append(point_h)
    # Вычисляем координаты прямоугольника для создания рта (Элипс вписанный в прямоугольник)
    point_left_bottom = sd.get_point(x - 35, y - 35)
    point_right_top = sd.get_point(x + 35, y - 15)
    # Вычисление и получение КООРДИНАТЫ ДЛЯ ГЛАЗ
    point_center_left_yae = sd.get_point(x - 20, y + 20)
    point_center_rihgt_yae = sd.get_point(x + 20, y + 20)
    # Рисуем НОС по координатам центра
    sd.circle(point_center, radius=5, color=sd.random_color(), width=2)
    # Рисуем ГЛАЗА
    sd.circle(point_center_left_yae, radius=5, color=sd.random_color(), width=2)
    sd.circle(point_center_rihgt_yae, radius=5, color=sd.random_color(), width=2)
    # Рисуем РОТ
    sd.ellipse(left_bottom=point_left_bottom, right_top=point_right_top, width=0)
    # Рисуем ТЕЛО смайлика
    sd.polygon(points, color=color, width=width)


for i in range(10):
    point_smilley_x = rd.randint(50, 1150)
    point_smilley_y = rd.randint(50, 750)
    color_smilley = sd.random_color()
    smiley_draw(point_smilley_x, point_smilley_y, color_smilley, width=3)


for i in range(5):
    point_smilley_x = rd.randint(45, 1155)
    point_smilley_y = rd.randint(45, 735)
    color = sd.random_color()
    smiley_draw2(point_smilley_x, point_smilley_y, color=sd.COLOR_RED)

print(smiley_draw2.__doc__)

sd.pause()
