# -*- coding: utf-8 -*-
import random as rd
import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_DARK_CYAN

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 25


def initial_snowfall(quantity):

    """
    Создаёт словарь списков координат и рандомной длины лучей новых снежинок.
    Принимает количество снежинок
    """
    dictionary_of_new_snowflake = {}
    for k in range(quantity):
        x = rd.randint(50, 1150)
        y = rd.randint(400, 750)
        length_of_branch = rd.randint(20, 60)
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


# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


initial_coordinates = initial_snowfall(N)

while True:
    sd.start_drawing()

    for j in initial_coordinates:
        drawing_snowflake(initial_coordinates[j])

    sd.finish_drawing()

    sd.sleep(0.1)
    sd.start_drawing()

    for j in initial_coordinates:
        if initial_coordinates[j][1] <= initial_coordinates[j][2]:
            initial_coordinates[j] = change_coordinates_of_an_existing_snowflake(initial_coordinates[j])
        else:
            drawing_snowflake(initial_coordinates[j], color=sd.background_color)

            initial_coordinates[j][0] += rd.randint(-10, 10)
            initial_coordinates[j][1] -= rd.randint(2, 20)

    sd.finish_drawing()

    if sd.user_want_exit():
        break

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
