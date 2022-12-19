# -*- coding: utf-8 -*-

import simple_draw as sd


# sd.resolution = (1600, 1000)


def draw_the_wall(inc_point_x, inc_point_y, width, step, height):
    """Рисует кирпичную стену по заданным размерам стены"""

    height = height - (height % step)
    width = width - (width % (step * 2))
    left_bottom = sd.get_point(inc_point_x, inc_point_y - 2)
    right_top = sd.get_point(inc_point_x + width + 2, inc_point_y + height)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_WHITE, width=2)
    for i in range(inc_point_y, height + inc_point_y + 1, step):
        start_point = sd.get_point(inc_point_x, i)
        stop_point = sd.get_point(width + inc_point_x, i)
        sd.line(start_point=start_point, end_point=stop_point, color=sd.COLOR_WHITE, width=2)

    for a in range(inc_point_y, height + inc_point_y, step * 2):
        for j in range(inc_point_x, width + inc_point_x + step, step * 2):
            start_point2 = sd.get_point(j, a)
            stop_point2 = sd.get_point(j, a + step)
            sd.line(start_point=start_point2, end_point=stop_point2, color=sd.COLOR_WHITE, width=2)

        for k in range(inc_point_x + step, width + inc_point_x, step * 2):
            if a + step >= height + inc_point_y:
                break
            start_point1 = sd.get_point(k, a + step)
            stop_point1 = sd.get_point(k, a + step * 2)
            sd.line(start_point=start_point1, end_point=stop_point1, color=sd.COLOR_WHITE, width=2)


# draw_the_wall(inc_point_x=350, inc_point_y=250, width=740, step=15, heihgt=520)


# sd.pause()
