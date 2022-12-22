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


def draw_the_roof(start_point, width_wall, height_wall, shift_roof, width=0):

    """Рисует треугольную крышу цветом color"""

    color = sd.COLOR_DARK_ORANGE
    # shift_roof = width_wall * 0.1
    width_roof = width_wall + shift_roof * 2
    height_roof = height_wall * 0.3 + width_wall * 0.2
    points = []
    # Получаем точки для рисования многоугольника
    point_a = start_point
    point_b = sd.get_point(start_point.x + width_roof, start_point.y)
    point_c = sd.get_point(start_point.x + width_roof / 2, start_point.y + height_roof)
    # Добавление координат вершин в список
    points.append(point_a)
    points.append(point_b)
    points.append(point_c)

    sd.polygon(points, color=color, width=width)

    # Рисуем вентиляционное окно
    point_window = sd.get_point(point_c.x, start_point.y + height_roof / 2.2)
    sd.circle(center_position=point_window, radius=height_roof / 4, color=sd.COLOR_WHITE, width=0)


def draw_the_house(start_point, quantity_bricks=15, width_wall=800, height_wall=300):

    """Рисует весь дом целиком из заданной точки"""

    height_wall = draw_wall(start_point=start_point, quantity_bricks=quantity_bricks,
                            width_wall=width_wall, height_wall=height_wall)

    shift_the_roof = width_wall * 0.1

    start_point_for_roof = sd.get_point(start_point.x - shift_the_roof, start_point.y + height_wall)
    draw_the_roof(start_point=start_point_for_roof,
                  width_wall=width_wall,
                  height_wall=height_wall,
                  shift_roof=shift_the_roof)
    return shift_the_roof


def main():
    sd.resolution = (1600, 800)
    sd.background_color = sd.COLOR_BLUE

    width_wall = 500
    height_wall = 400
    point_start = sd.get_point(400, 1600 / 10)
    draw_the_house(start_point=point_start, width_wall=width_wall, height_wall=height_wall)

    sd.pause()


if __name__ == '__main__':
    main()
