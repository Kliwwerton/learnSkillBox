# -*- coding: utf-8 -*-

import simple_draw as sd
from random import choice

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные


def draw_the_rainbow(point, radius, width=8):
    """Рисует радугу """
    for _ in range(7):
        rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                          sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
        random_color = choice(rainbow_colors)

        radius -= width
        sd.circle(center_position=point, radius=radius, width=width, color=random_color)


def draw_the_snowflake(_x, _y, length=15, color=sd.COLOR_WHITE):
    """Рисует снежинку в координатах X, Y цветом COLOR"""
    point = sd.get_point(_x, _y)
    sd.snowflake(center=point, length=length, color=color)


def draw_the_sun(point, corner, color=sd.COLOR_YELLOW):
    """Рисует солнышко в заданной точке"""
    sd.circle(center_position=point, width=0)
    for i in range(corner, corner + 360, 30):
        line = sd.get_vector(start_point=point, angle=i, width=3)
        line.draw(color)


def draw_the_animation(number_of_snowflakes, height_plot, center_rainbow, radius, center_sun):
    y = 500
    corner = 0
    while True:
        points = []
        length = 15
        for i in range(number_of_snowflakes):
            x = sd.random_number(15, 250)
            points.append(x)
        sd.start_drawing()
        draw_the_sun(center_sun, corner=corner - 15, color=sd.background_color)
        if corner > 359:
            corner = 0
        draw_the_sun(center_sun, corner)
        sd.finish_drawing()

        while True:
            sd.start_drawing()

            for x in points:
                if y < height_plot + length * 3:
                    continue
                draw_the_snowflake(_x=x, _y=y, color=sd.background_color)
            y -= 5
            for i in range(number_of_snowflakes):
                points[i] += sd.random_number(-1, 1)
            for x in points:
                draw_the_snowflake(_x=x, _y=y, length=length)
            if y < height_plot + length:
                break
            draw_the_rainbow(center_rainbow, radius=radius)
            sd.finish_drawing()
            sd.sleep(0.025)

            if sd.user_want_exit():
                break
        corner += 15
        y = 500
        if sd.user_want_exit():
            break
