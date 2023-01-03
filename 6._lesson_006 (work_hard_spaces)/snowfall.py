#  -*- coding: utf-8 -*-

import simple_draw as sd
import random as rd

# sd.resolution = (1200, 800)


def initial_snowfall(quantity, min_point, max_point):

    """
    Создаёт словарь списков координат и рандомной длины лучей новых снежинок.
    Принимает количество снежинок и координаты диапазонаЖ
     min_point - нижняя левая точка диапазона
     max_point - верхняя правая точка диапазона.
    """
    dictionary_of_new_snowflakes = {}
    for k in range(quantity):
        length_of_branch = rd.randint(10, 20)
        x = rd.randint(min_point.x + length_of_branch, max_point.x)
        y = rd.randint(min_point.y + length_of_branch, max_point.y)
        dictionary_of_new_snowflakes[k] = [x, y, length_of_branch]

    return dictionary_of_new_snowflakes


def drawing_snowflake(dict_of_coordinates, color=sd.COLOR_WHITE):

    """Рисует снежинку. Принимает словарь из списка координат и длины лучей и цвет."""

    for i in dict_of_coordinates:
        point_of_snowflake = sd.get_point(dict_of_coordinates[i][0], dict_of_coordinates[i][1])
        sd.snowflake(center=point_of_snowflake, length=dict_of_coordinates[i][2], color=color)


def shift_snowflakes(dict_of_coordinates):

    """ Сдвигает снежинки вниз с рандомной скоростью,
    также сдвигая немного их и по горизонтали, создавая эффект завихрения.
    Принимает словарь со списками информации о снежинках."""

    for i in dict_of_coordinates:
        dict_of_coordinates[i][0] += rd.randint(-10, 10)
        if dict_of_coordinates[i][0] > sd.resolution[0]:
            dict_of_coordinates[i][0] -= 10
        elif dict_of_coordinates[i][0] < 0:
            dict_of_coordinates[i][0] += 10

        dict_of_coordinates[i][1] -= rd.randint(2, 10)

    return dict_of_coordinates


def check_coordinates(dict_of_snowflakes):

    """ Проверяет координаты снежинок, если снежинка падает ниже нижнего края экрана, добавляет её в новый список. """

    fall_list = []
    for i in dict_of_snowflakes:
        if dict_of_snowflakes[i][1] < 20:
            fall_list.append(i)

    return fall_list


def create_snowflake(dict_of_snowflakes, list_of_snowflakes):

    """ Создаёт снежинку в заданной точке.
    Принимает словарь с существующими снежинками и список ключей, удалённых списков из этого словаря.
     Взамен создаёт новую снежинку на месте удалённой. """

    for i in list_of_snowflakes:
        length_of_branch = rd.randint(10, 20)
        x = rd.randint(20, sd.resolution[0]-20)
        y = sd.resolution[1]-20
        dict_of_snowflakes[i] = [x, y, length_of_branch]

    return dict_of_snowflakes


def main():
    n = 500  # количество снежинок
    min_point = sd.get_point(20, 20)
    max_point = sd.get_point(sd.resolution[0]-20, sd.resolution[1]-20)
    snowflakes = initial_snowfall(quantity=n, min_point=min_point, max_point=max_point)

    while True:
        sd.start_drawing()

        drawing_snowflake(snowflakes, color=sd.background_color)
        shift_snowflakes(dict_of_coordinates=snowflakes)
        drawing_snowflake(dict_of_coordinates=snowflakes)

        sd.finish_drawing()
        if sd.user_want_exit(sleep_time=0.01):
            break


if __name__ == '__main__':
    main()
