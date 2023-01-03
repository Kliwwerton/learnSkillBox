# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py, в котором реализовать следующие функции:
#    создать_снежинки(N) - создает N снежинок
#    нарисовать_снежинки_цветом (color) - отрисовывает все снежинки цветом color
#    сдвинуть_снежинки() - сдвигает снежинки на один шаг
#    номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#    удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
n = 50
snowflakes = snowfall.initial_snowfall(quantity=n,
                                       min_point=sd.get_point(20, 20),
                                       max_point=sd.get_point(sd.resolution[0]-20, sd.resolution[1]-20))
while True:
    sd.start_drawing()

    snowfall.drawing_snowflake(dict_of_coordinates=snowflakes, color=sd.background_color)
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    snowfall.shift_snowflakes(dict_of_coordinates=snowflakes)
    #  сдвинуть_снежинки()
    snowfall.drawing_snowflake(dict_of_coordinates=snowflakes, color=sd.random_color())
    #  нарисовать_снежинки_цветом(color)
    snowfall.check_coordinates(snowflakes)
    #  если есть номера_достигших_низа_экрана() то
    fall_snowflakes = snowfall.check_coordinates(snowflakes)
    if fall_snowflakes:
        for i in fall_snowflakes:
            del snowflakes[i]
        # удалить_снежинки(номера)
        snowfall.create_snowflake(snowflakes, fall_snowflakes)

    sd.finish_drawing()

    if sd.user_want_exit(sleep_time=0.1):
        break

# sd.pause()
