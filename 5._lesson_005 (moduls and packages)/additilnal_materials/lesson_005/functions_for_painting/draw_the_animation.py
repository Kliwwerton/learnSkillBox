# -*- coding: utf-8 -*-

import random as rd
import simple_draw as sd


def draw_the_sun(x=150, y=600, beam=100, corner_beam_sun=0, color=sd.COLOR_YELLOW, width=3):
    point = sd.get_point(x=x, y=y)
    sd.circle(center_position=point, color=color, width=0)

    for i in range(corner_beam_sun, 360 + corner_beam_sun, 30):
        sd.vector(start=point, angle=i, length=beam, color=color, width=width)


rainbow_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]


def painting_rainbow_animation(_x=400, _y=-100, radius=1000, step=5):
    center = sd.get_point(x=_x, y=_y)
    rd.shuffle(rainbow_colors)
    for j in rainbow_colors:
        sd.circle(center_position=center, radius=radius, color=j, width=step)
        radius -= step


def initial_snowfall(quantity, min_point, max_point):

    """
    Создаёт словарь списков координат и рандомной длины лучей новых снежинок.
    Принимает количество снежинок
    """
    dictionary_of_new_snowflakes = {}
    for k in range(quantity):
        length_of_branch = rd.randint(10, 20)
        x = rd.randint(min_point.x + length_of_branch, max_point.x)
        y = rd.randint(min_point.y + length_of_branch, max_point.y)
        coordinates_of_new_snowflake = [x, y, length_of_branch]
        dictionary_of_new_snowflakes[k] = coordinates_of_new_snowflake
    return dictionary_of_new_snowflakes


def change_coordinates_of_an_existing_snowflake(list_of_parameters, min_, max_):

    """
    Принимает словарь координат снежинок, проверяет, достигли ли они нижнего края экрана.
    Если снежинка достигла нижней границы экрана, создаёт новую в верхней части экрана.
    :return: Список новых координат и размера снежинки.
    """
    list_of_parameters[0] = rd.randint(min_.x, max_.x)
    list_of_parameters[2] = rd.randint(10, 20)
    list_of_parameters[1] = max_.y - list_of_parameters[2]

    return list_of_parameters


def drawing_snowflake(list_of_coordinates, color=sd.COLOR_WHITE):

    """Рисует снежинку. Принимает список координат, длину лучиков и цвет."""

    point_of_snowflake = sd.get_point(list_of_coordinates[0], list_of_coordinates[1])
    sd.snowflake(center=point_of_snowflake, length=list_of_coordinates[2], color=color)


def main(min_point, max_point, height_earth, radius_rainbow):
    n = 40  # количество снежинок
    corner_beam_sun = 0  # Угол отклонения лучей солнца
    initial_coordinates = initial_snowfall(quantity=n, min_point=min_point, max_point=max_point)
    step = 0
    change_number = rd.randint(0, 10)
    while True:
        sd.start_drawing()

        for j in initial_coordinates:
            if initial_coordinates[j][1] <= initial_coordinates[j][2] + height_earth:
                initial_coordinates[j] = change_coordinates_of_an_existing_snowflake(initial_coordinates[j],
                                                                                     min_point, max_point)
            else:
                drawing_snowflake(initial_coordinates[j], color=sd.background_color)

                initial_coordinates[j][0] += rd.randint(-10, 10)
                if initial_coordinates[j][0] > max_point.x:
                    initial_coordinates[j][0] -= 10
                elif initial_coordinates[j][0] < min_point.x:
                    initial_coordinates[j][0] += 10

                initial_coordinates[j][1] -= rd.randint(2, 10)

        for j in initial_coordinates:
            drawing_snowflake(initial_coordinates[j])

        if change_number == step:
            painting_rainbow_animation(_y=-600, radius=radius_rainbow, step=15)

        if step > 10:
            draw_the_sun(y=700, corner_beam_sun=corner_beam_sun - 15, color=sd.background_color, width=6)
            draw_the_sun(y=700, corner_beam_sun=corner_beam_sun)
            corner_beam_sun += 15
            step = 0
            change_number = rd.randint(0, 10)
            if corner_beam_sun > 360:
                corner_beam_sun = 0

        sd.finish_drawing()
        step += 1
        # sd.sleep(0.1)
        if sd.user_want_exit(sleep_time=0.1):
            break


if __name__ == '__main__':
    width_window = 1600
    height_window = 800
    sd.resolution = (width_window, height_window)
    sd.background_color = sd.COLOR_DARK_CYAN
    point_1 = sd.get_point(0, 80)
    point_2 = sd.get_point(1040, 570)
    main(min_point=point_1, max_point=point_2, height_earth=80, radius_rainbow=width_window)

    sd.pause()
