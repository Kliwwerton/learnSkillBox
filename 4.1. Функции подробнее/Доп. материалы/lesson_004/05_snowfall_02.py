# -*- coding: utf-8 -*-
import random as rd
import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_PURPLE

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

initial_coordinates = {}

for i in range(N):
    x = rd.randint(50, 1150)
    y = rd.randint(400, 750)
    length_of_branch = rd.randint(20, 60)
    coordinates = [x, y, length_of_branch]
    initial_coordinates[i] = coordinates

second_coordinates = initial_coordinates.copy()

while True:
    sd.start_drawing()

    for i in initial_coordinates:
        point = sd.get_point(initial_coordinates[i][0], initial_coordinates[i][1])
        sd.snowflake(center=point, length=initial_coordinates[i][2])

    # second_coordinates = initial_coordinates.copy()
    sd.finish_drawing()

    sd.sleep(0.1)
    sd.start_drawing()
    # for j in initial_coordinates:
    #     if initial_coordinates[j][1] > initial_coordinates[j][2]:
    #         point = sd.get_point(initial_coordinates[j][0], initial_coordinates[j][1])
    #         sd.snowflake(center=point, length=initial_coordinates[j][2], color=sd.background_color)
    for i in initial_coordinates:
        if initial_coordinates[i][1] <= initial_coordinates[i][2]:
            initial_coordinates[i][1] = 800 - initial_coordinates[i][2]
            initial_coordinates[i][0] = rd.randint(50, 1150)
        else:
            point = sd.get_point(initial_coordinates[i][0], initial_coordinates[i][1])
            sd.snowflake(center=point, length=initial_coordinates[i][2], color=sd.background_color)
            initial_coordinates[i][0] += rd.randint(-10, 10)
            initial_coordinates[i][1] -= rd.randint(2, 20)

    sd.finish_drawing()

    if sd.user_want_exit():
        break


# while True:
#     sd.clear_screen()
#     point = sd.get_point(x, y)
#     sd.snowflake(center=point, length=50)
#     y -= 10
#     if y < 50:
#         break
#     x = x + 7
#
#     point2 = sd.get_point(x2, y2)
#     sd.snowflake(center=point2, length=30)
#     y2 -= 10
#     if y2 < 50:
#         break
#     x2 = x2 + 12
#
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


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
