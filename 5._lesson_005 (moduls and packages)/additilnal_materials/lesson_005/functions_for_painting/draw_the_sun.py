# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_the_sun(x=150, y=600, beam=100):
    point = sd.get_point(x=x, y=y)
    sd.circle(center_position=point, color=sd.COLOR_YELLOW, width=0)

    for i in range(0, 360, 30):
        sd.vector(start=point, angle=i, length=beam, color=sd.COLOR_YELLOW, width=3)
