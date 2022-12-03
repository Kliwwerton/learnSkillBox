#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint


sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']


moscow_london = ((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5
moscow_paris = ((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

london_moscow = ((london[0] - moscow[0]) ** 2 + (london[1] - moscow[1]) ** 2) ** 0.5
london_paris = ((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5

distances['London'] = {}
distances['London']['Moscow'] = london_moscow
distances['London']['Paris'] = london_paris


paris_moscow = ((paris[0] - moscow[0]) ** 2 + (paris[1] - moscow[1]) ** 2) ** 0.5
paris_london = ((paris[0] - london[0]) ** 2 + (paris[1] - london[1]) ** 2) ** 0.5

distances['Paris'] = {}
distances['Paris']['Moscow'] = paris_moscow
distances['Paris']['London'] = paris_london

for i in distances:
    print(distances[i])

pprint(distances)


