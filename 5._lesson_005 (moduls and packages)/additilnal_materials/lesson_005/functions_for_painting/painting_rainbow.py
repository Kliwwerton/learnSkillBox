# -*- coding: utf-8 -*-

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def painting_rainbow(x=200, y=-100, radius=1000, step=5):
    center = sd.get_point(x=x, y=y)
    for i in rainbow_colors:
        sd.circle(center_position=center, radius=radius, color=i, width=step)
        radius -= step
