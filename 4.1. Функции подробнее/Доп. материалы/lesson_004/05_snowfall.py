# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)
sd.background_color = sd.COLOR_PURPLE
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 30

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def draw_the_snowflake(_x, _y, length=30, color=sd.COLOR_WHITE):
    """Рисует снежинку в координатах X, Y цветом COLOR"""
    point = sd.get_point(_x, _y)
    sd.snowflake(center=point, length=length, color=color)


for i in range(40, 1200, 40):
    point_0 = sd.get_point(i, 750)
    sd.circle(center_position=point_0, color=sd.COLOR_BLACK, width=0)


y = 685

while True:
    points = []
    for i in range(N):
        x = sd.random_number(20, 1180)
        points.append(x)

    while True:
        sd.start_drawing()
        for x in points:
            if y < 60:
                continue
            draw_the_snowflake(_x=x, _y=y, color=sd.background_color)
        y -= 5
        for i in range(N):
            if points[i] > 1200:
                points[i] -= 1200
            elif points[i] < 0:
                points[i] += 1200
            points[i] += sd.random_number(-5, 5)
        for x in points:
            draw_the_snowflake(_x=x, _y=y)
        if y < 30:
            break
        sd.finish_drawing()
        sd.sleep(0.025)

        if sd.user_want_exit():
            break
    y = 685
    if sd.user_want_exit():
        break


sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


