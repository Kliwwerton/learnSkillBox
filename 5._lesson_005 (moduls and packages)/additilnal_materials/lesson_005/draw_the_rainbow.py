# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_the_rainbow(point, radius, width=8):
    """Рисует радугу """
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                      sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    for i in rainbow_colors:
        radius -= width
        sd.circle(center_position=point, radius=radius, width=width, color=i)
