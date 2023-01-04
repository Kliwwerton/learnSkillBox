# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 800)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    """ Класс Снежинки """

    def __init__(self,
                 x=random.randint(20, sd.resolution[0] - 20),
                 y=sd.resolution[1] - 20,
                 length=100,
                 color=sd.COLOR_WHITE):
        self.x = x
        self.y = y
        self.point = sd.get_point(x=self.x, y=self.y)
        self.length = length
        self.color = color

    def draw(self):
        """Рисует снежинку на полотне"""
        sd.snowflake(center=self.point, length=self.length, color=self.color)

    def move(self):
        """Сдвигает снежинку вниз по экрану"""
        self.x += random.randint(-10, 10)
        self.y -= random.randint(2, 10)
        self.point = sd.get_point(self.x, self.y)

    def can_fall(self):
        """Проверяем, может ли снежинка продолжать падение"""
        return self.y >= self.length

    def clear_previous_picture(self):
        sd.snowflake(center=self.point, length=self.length, color=sd.background_color)


def get_flakes(count=1):
    list_snowflakes = []
    for i in range(count):
        snowflake = Snowflake(length=random.randint(10, 30))
        list_snowflakes.append(snowflake)
    return list_snowflakes


def get_fallen_flakes():
    pass


def append_flakes():
    pass


# flake = Snowflake(length=30)
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#
#     if sd.user_want_exit(sleep_time=0.1):
#         break

n = 30

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

flakes = get_flakes(count=n)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху

    if sd.user_want_exit(sleep_time=0.1):
        break

sd.pause()
