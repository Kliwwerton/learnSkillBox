# -*- coding: utf-8 -*-

import simple_draw as sd


def draw_the_sun(x=150, y=600, beam=100, corner_beam_sun=0, color=sd.COLOR_YELLOW, width=3):
    point = sd.get_point(x=x, y=y)
    sd.circle(center_position=point, color=color, width=0)

    for i in range(corner_beam_sun, 360 + corner_beam_sun, 30):
        sd.vector(start=point, angle=i, length=beam, color=color, width=width)
