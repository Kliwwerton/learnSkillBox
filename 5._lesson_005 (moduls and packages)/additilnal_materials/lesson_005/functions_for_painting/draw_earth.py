# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_the_earth(width, length):
    start_point = sd.get_point(0, 0)
    end_point = sd.get_point(width, length)

    sd.rectangle(left_bottom=start_point, right_top=end_point, color=(47, 79, 79))
