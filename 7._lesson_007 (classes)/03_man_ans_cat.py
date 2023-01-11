# -*- coding: utf-8 -*-

import random as rd

import colorama
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризуется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   Купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу) :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def cleans(self):
        self.fullness -= 10
        self.house.dirt -= 25

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='blue')

    @staticmethod
    def get_cat(_cat, house):
        _cat.go_to_the_house(house=house)

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = rd.randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.dirt > 50:
            self.cleans()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 0:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_mtv()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_for_cat = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме человеческой еды {}, для кота {}, денег {}, грязи {}'.format(
            self.food, self.food_for_cat, self.money, self.dirt)

    def check(self):
        if self.dirt < 0:
            self.dirt = 0


class Cat:
    """ Класс кота """

    def __init__(self, name):
        self.fullness = 100
        self.name = name
        self.house = None

    def __str__(self):
        return f'Я {self.name}, моя сытость {self.fullness}'

    def act(self):
        pass

    def play(self):
        self.fullness -= 10
        self.house.dirt += 5

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        print(colorama.Fore.RED + f'{self.name} поселился в доме!', colorama.Style.RESET_ALL)


citizens = [
    Man(name='Бивис'),
    # Man(name='Батхед'),
    # Man(name='Кенни'),
]
cat = Cat(name='Мурзик')
my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)
citizens[0].get_cat(_cat=cat, house=my_sweet_home)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()
    cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    print(cat)

    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
