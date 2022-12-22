# -*- coding: utf-8 -*-
import random
import simple_draw as sd


def draw_snowdrift(start_point, end_point):

    """ Рисует кучу снежинок в диапазоне координат.
    Принимает две точки: 1. начала зоны рисования, 2. Конец зоны рисования. """

    quantity_snowflakes = (end_point.x - start_point.x) // 10

    for i in range(quantity_snowflakes):
        beam_of_snowflake = random.randint(10, 30)
        x = random.randint(start_point.x + beam_of_snowflake, end_point.x - beam_of_snowflake)
        y = random.randint(start_point.y + beam_of_snowflake, end_point.y + beam_of_snowflake * 2)
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=beam_of_snowflake)


def main():
    draw_snowdrift(start_point=sd.get_point(100, 30),
                   end_point=sd.get_point(700, 30),
                   )


if __name__ == '__main__':
    sd.resolution = (1200, 800)

    main()

    sd.pause()
