# -*- coding: utf-8 -*-

import simple_draw as sd
import random


def draw_tree(start_point, length_branch=120, corner=90, width=10, color=sd.COLOR_DARK_ORANGE):

    """Draws a tree with random length of branch"""

    branch = sd.vector(start=start_point, angle=corner, length=length_branch, width=width, color=color)
    length_branch *= (0.75 + (random.randint(-10, 10)/100))
    alpha = corner + random.randint(-50, 0)
    betta = corner + random.randint(0, 50)
    if width > 2:
        width -= 2
    if length_branch < 7:
        color = sd.COLOR_DARK_GREEN
    if length_branch > 5:
        draw_tree(start_point=branch, length_branch=length_branch, corner=alpha, width=width, color=color)
        draw_tree(start_point=branch, length_branch=length_branch, corner=betta, width=width, color=color)

