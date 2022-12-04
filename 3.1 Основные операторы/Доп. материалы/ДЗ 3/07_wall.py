# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.background_color = sd.COLOR_DARK_PURPLE

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for
sd.resolution = (1200, 800)
x = 0
a = 0
step = 20
y = step
for i in range(0, sd.resolution[0] + 1, step):
    start_point = sd.get_point(x, i)
    stop_point = sd.get_point(sd.resolution[0], i)
    sd.line(start_point=start_point, end_point=stop_point, color=sd.COLOR_WHITE, width=2)

for a in range(x, sd.resolution[1], step * 2):
    for j in range(0, sd.resolution[0], step * 2):
        start_point2 = sd.get_point(j, a)
        stop_point2 = sd.get_point(j, step + a)
        sd.line(start_point=start_point2, end_point=stop_point2, color=sd.COLOR_WHITE, width=2)

    for k in range(step, sd.resolution[0], step * 2):
        start_point2 = sd.get_point(k, y + a)
        stop_point2 = sd.get_point(k, y + step + a)
        sd.line(start_point=start_point2, end_point=stop_point2, color=sd.COLOR_WHITE, width=2)

    a += step * 2

sd.pause()
