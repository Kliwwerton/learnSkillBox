# -*- coding: utf-8 -*-

import simple_draw as sd
import numpy


def draw_wall(start_point, quantity_bricks, width_wall, height_wall, color=sd.COLOR_BLACK):

    """ Рисует стену из кирпичей из заданной точки заданной высоты, длины из заданного количества кирпичей.
     Возвращает высоту стены.
    Высота стены - height_wall
    Ширина стены - width_wall
    Количество кирпичей по длине стены - quantity_bricks
    """
    length_brick = round(width_wall / quantity_bricks, 2)
    height_brick = int(length_brick / 2)
    height_wall = int((height_wall // height_brick) * height_brick)
    length_wall = length_brick * quantity_bricks

    print(f'Высота стены:', {height_wall},
          'Ширина стены:', {length_wall},
          'Длина кирпича:', {length_brick},
          'Высота кирпича:', {height_brick})

    sd.rectangle(left_bottom=start_point,
                 right_top=sd.get_point(start_point.x+(length_brick*quantity_bricks)+2, start_point.y+height_wall+2),
                 width=2, color=color)

    a = 1
    for i in range(start_point.y+2, height_wall+start_point.y, height_brick):
        if a % 2 == 1:
            for j in numpy.arange(start_point.x+2, width_wall+start_point.x, length_brick):
                point_start = sd.get_point(j - 2, i - 2)
                point_finish = sd.get_point(j + length_brick, i + height_brick)
                sd.rectangle(left_bottom=point_start, right_top=point_finish, color=color, width=2)
        else:
            for j in numpy.arange(start_point.x + 2, width_wall + start_point.x - length_brick, length_brick):
                point_start = sd.get_point(j - 2 + length_brick / 2, i - 2)
                point_finish = sd.get_point(j + length_brick * 1.5, i + height_brick)
                sd.rectangle(left_bottom=point_start, right_top=point_finish, color=color, width=2)
        a += 1

    return height_wall+2


def draw_the_roof(start_point, corner=30, length_side=150):

    """Рисует крышу дома"""

    side = sd.vector(start=start_point, angle=corner, length=length_side, width=2)
    corner += 360 / 3
    side_2 = sd.vector(start=side, angle=corner, length=length_side, width=2)
    corner += 360 / 3
    sd.vector(start=side_2, angle=corner, length=length_side, width=2)


def draw_the_house(start_point, quantity_bricks=15, width_wall=300, height_wall=300):

    """Рисует весь дом целиком из заданной точки"""

    height_wall = draw_wall(start_point=start_point, quantity_bricks=quantity_bricks,
                            width_wall=width_wall, height_wall=height_wall)

    start_point_for_roof = sd.get_point(start_point.x - width_wall//3, start_point.y + height_wall)
    draw_the_roof(start_point=start_point_for_roof, corner=0, length_side=width_wall + (width_wall//3) * 2)
