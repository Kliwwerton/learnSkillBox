# -*- coding: utf-8 -*-

import random as rd
import simple_draw as sd


def initial_snowfall(quantity):

    """
    Создаёт словарь списков координат и рандомной длины лучей новых снежинок.
    Принимает количество снежинок
    """
    dictionary_of_new_snowflake = {}
    for k in range(quantity):
        x = rd.randint(50, 1150)
        y = rd.randint(400, 750)
        length_of_branch = rd.randint(10, 30)
        coordinates_of_new_snowfall = [x, y, length_of_branch]
        dictionary_of_new_snowflake[k] = coordinates_of_new_snowfall
    return dictionary_of_new_snowflake


def change_coordinates_of_an_existing_snowflake(list_of_parameters):

    """
    Принимает словарь координат снежинок, проверяет, достигли ли они нижнего края экрана.
    Если снежинка достигла нижней границы экрана, создаёт новую в верхней части экрана.
    :return: словарь снежинок.
    """
    list_of_parameters[0] = rd.randint(50, 1150)
    list_of_parameters[2] = rd.randint(10, 60)
    list_of_parameters[1] = 800 - list_of_parameters[2]

    return list_of_parameters


def drawing_snowflake(list_of_coordinates, color=sd.COLOR_WHITE):

    """Рисует снежинку. Принимает список координат, длину лучиков и цвет."""

    point_of_snowflake = sd.get_point(list_of_coordinates[0], list_of_coordinates[1])
    sd.snowflake(center=point_of_snowflake, length=list_of_coordinates[2], color=color)


def draw_snowfall(initial_coordinates):
    while True:
        sd.start_drawing()

        for j in initial_coordinates:
            if initial_coordinates[j][1] <= initial_coordinates[j][2]:
                initial_coordinates[j] = change_coordinates_of_an_existing_snowflake(initial_coordinates[j])
            else:
                drawing_snowflake(initial_coordinates[j], color=sd.background_color)

                initial_coordinates[j][0] += rd.randint(-10, 10)
                initial_coordinates[j][1] -= rd.randint(2, 20)

        for j in initial_coordinates:
            drawing_snowflake(initial_coordinates[j])

        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


def main():
    n = 20  # количество снежинок
    initial_coordinates = initial_snowfall(n)
    draw_snowfall(initial_coordinates)


if __name__ == '__main__':
    sd.resolution = (1200, 800)
    sd.background_color = sd.COLOR_DARK_CYAN
    main()

    sd.pause()
