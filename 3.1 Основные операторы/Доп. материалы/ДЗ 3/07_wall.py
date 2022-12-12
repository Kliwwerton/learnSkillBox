# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.background_color = sd.COLOR_WHITE

x, y = 1200, 800

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (x, y)

# x = 0
# a = 0
# step = 20
# y = step
# for i in range(0, sd.resolution[0] + 1, step):
#     start_point = sd.get_point(x, i)
#     stop_point = sd.get_point(sd.resolution[0], i)
#     sd.line(start_point=start_point, end_point=stop_point, color=sd.COLOR_WHITE, width=2)
#
# for a in range(x, sd.resolution[1], step * 2):
#     for j in range(0, sd.resolution[0], step * 2):
#         start_point2 = sd.get_point(j, a)
#         stop_point2 = sd.get_point(j, step + a)
#         sd.line(start_point=start_point2, end_point=stop_point2, color=sd.COLOR_WHITE, width=2)
#
#     for k in range(step, sd.resolution[0], step * 2):
#         start_point2 = sd.get_point(k, y + a)
#         stop_point2 = sd.get_point(k, y + step + a)
#         sd.line(start_point=start_point2, end_point=stop_point2, color=sd.COLOR_WHITE, width=2)
#
#     a += step * 2

quantity_bricks = 30

length_brick = x // quantity_bricks
height_brick = int(length_brick / 2)
height_wall = int((y // height_brick)*height_brick)

print(length_brick, height_brick, height_wall)
a = 1
for i in range(0, height_wall, height_brick):
    for j in range(- length_brick, x, length_brick):
        if a % 2 == 1:
            point_start = sd.get_point(j - 2, i - 2)
            point_finish = sd.get_point(j + length_brick, i + height_brick)
        else:
            point_start = sd.get_point(j - 2 + length_brick / 2, i - 2)
            point_finish = sd.get_point(j + length_brick * 1.5, i + height_brick)
        sd.rectangle(left_bottom=point_start, right_top=point_finish, color=sd.COLOR_RED, width=2)
    a += 1
sd.pause()
