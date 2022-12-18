# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_the_roof(start_point_x, start_point_y, width_roof, height_roof, color, width=0):
    """Рисует треугольную крышу цветом color"""
    points = []
    # Получаем точки для рисования многоугольника
    point_a = sd.get_point(start_point_x, start_point_y)
    point_b = sd.get_point(start_point_x + width_roof, start_point_y)
    point_c = sd.get_point(start_point_x + width_roof / 2, start_point_y + height_roof)
    # Добавление координат вершин в список
    points.append(point_a)
    points.append(point_b)
    points.append(point_c)

    sd.polygon(points, color=color, width=width)
