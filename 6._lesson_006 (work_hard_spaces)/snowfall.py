#  -*- coding: utf-8 -*-

import simple_draw as sd
import random as rd

sd.resolution = (1200, 800)
N = 50  # количество снежинок


def initial_snowfall(quantity, min_point, max_point, color=sd.COLOR_WHITE):

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
        sd.snowflake(center=sd.get_point(x, y), length=length_of_branch, color=color)
    return dictionary_of_new_snowflakes


def main():

    min_point = sd.get_point(20, 20)
    max_point = sd.get_point(sd.resolution[0]-20, sd.resolution[1]-20)
    snowflakes = initial_snowfall(quantity=N, min_point=min_point, max_point=max_point)
    while True:

        if sd.user_want_exit(sleep_time=0.1):
            break


if __name__ == '__main__':
    main()
