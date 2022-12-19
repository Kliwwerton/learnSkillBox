# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

import simple_draw as sd
import draw_the_wall
import draw_the_roof
import draw_the_trees
import draw_the_cloud
import draw_the_snow_rainbow_sun


width_of_the_canvas = 1600
height_of_the_canvas = 800

sd.resolution = (width_of_the_canvas, height_of_the_canvas)


def func_draw_the_cloud(x, y, x1, y1, color=sd.COLOR_WHITE):
    """Рисует облако в заданных координатах
    x, y = координаты нижнего левого угла прямоугольника вписываемого овала
    x1, y1 = координаты верхнего правого угла прямоугольника вписываемого овала"""
    point_cloud_left_bottom = sd.get_point(x, y)
    point_cloud_right_top = sd.get_point(x1, y1)
    points_cloud = [point_cloud_left_bottom, point_cloud_right_top]
    draw_the_cloud.draw_the_cloud(points_cloud, color)


def draw_the_Earth(height, width):
    """Рисует землю для расположения на ней домика и дерева."""
    sd.rectangle(left_bottom=sd.get_point(0, 0), right_top=sd.get_point(width, height), width=0, color=(47, 79, 79))


# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


def main(_width_of_the_canvas):
    """Инициализирует весь процесс рисования картины"""

    # Рисуем участок земли
    height_plot = 100
    draw_the_Earth(height=height_plot, width=_width_of_the_canvas)

    # Рисуем дом
    left_bottom = 300

    # Рисуем стену дома
    width_of_house = 600  # ширина домика
    height_of_house = 350  # высота домика
    thickness_of_brick = 25  # толщина кирпича
    draw_the_wall.draw_the_wall(inc_point_x=left_bottom, inc_point_y=height_plot, width=width_of_house,
                                height=height_of_house, step=thickness_of_brick)
    # Рисуем крышу
    shift_roof = 30
    color_of_roof = sd.COLOR_RED
    draw_the_roof.draw_the_roof(start_point_x=left_bottom - shift_roof,
                                start_point_y=height_plot + height_of_house,
                                width_roof=width_of_house + shift_roof * 2,
                                height_roof=height_of_house / 3,
                                color=color_of_roof)

    # Рисуем вентиляционное отверстие на крыше
    point_center = sd.get_point(left_bottom + width_of_house / 2, height_plot + height_of_house + 45)
    sd.circle(center_position=point_center, radius=30, width=0, color=sd.COLOR_WHITE)

    # Рисуем деревья
    root_point = sd.get_point(left_bottom + width_of_house + left_bottom, height_plot)
    draw_the_trees.draw_bunches(start_point=root_point, angle=90, length=60)
    root_point2 = sd.get_point(left_bottom + width_of_house + left_bottom * 1.5, height_plot)
    draw_the_trees.draw_bunches(start_point=root_point2, angle=90, length=50)

    # # Рисуем радугу
    # center_rainbow = sd.get_point(100, -100)
    # draw_the_rainbow.draw_the_rainbow(point=center_rainbow, radius=width_of_the_canvas)

    # Рисуем центральную часть облака
    func_draw_the_cloud(x=width_of_the_canvas * 0.6,
                        y=height_of_the_canvas - 150,
                        x1=width_of_the_canvas * 0.7,
                        y1=height_of_the_canvas - 30)

    # Рисуем левую часть облака
    func_draw_the_cloud(x=width_of_the_canvas * 0.6 - 70,
                        y=height_of_the_canvas - 150,
                        x1=width_of_the_canvas * 0.7 - 50,
                        y1=height_of_the_canvas - 50)

    # Рисуем правую часть облака
    func_draw_the_cloud(x=width_of_the_canvas * 0.6 + 60,
                        y=height_of_the_canvas - 130,
                        x1=width_of_the_canvas * 0.7 + 50,
                        y1=height_of_the_canvas - 50)

    # Рисуем чёрное облако
    func_draw_the_cloud(x=5,
                        y=500,
                        x1=250,
                        y1=600, color=sd.COLOR_BLACK)

    # Рисуем анимацию (идущий снег, мерцающую радугу и крутящиеся лучи солнца)
    center_sun = sd.get_point(120, 680)
    center_rainbow = sd.get_point(100, -100)
    draw_the_snow_rainbow_sun.draw_the_animation(number_of_snowflakes=10, height_plot=height_plot,
                                                 center_rainbow=center_rainbow, radius=width_of_the_canvas,
                                                 center_sun=center_sun)


main(width_of_the_canvas)

sd.pause()
