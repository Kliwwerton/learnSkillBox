# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_the_cloud(points, color, width=0):

    """Рисует облако"""

    sd.ellipse(left_bottom=points[0], right_top=points[1], color=color, width=width)
