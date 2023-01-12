# -*- coding: utf-8 -*-

import random as rd

import colorama
from termcolor import cprint

RESET = colorama.Style.RESET_ALL
COLORED = colorama.Fore

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
            self.fullness += 30
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def cleans(self):
        print(colorama.Fore.LIGHTBLACK_EX + f'{self.name} прибрался за котом!' + colorama.Style.RESET_ALL)
        self.fullness -= 10
        self.house.dirt -= 25

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def watch_mtv(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 5

    def shopping(self):
        if self.house.money >= 50 and self.house.food < 10:
            print('{} сходил в магазин за едой'.format(self.name))
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 5
        elif self.house.food < 10:
            print(COLORED.RED + f'{self.name} деньги кончились, куплю на кредитку' + RESET)
            self.house.money -= 50
            self.house.food += 50
            self.fullness -= 5
        if self.house.money >= 20 and self.house.food_for_cat < 10:
            print(colorama.Fore.GREEN + f'{self.name}, сходил за кормом для кота!' + RESET)
            self.house.money -= 20
            self.house.food_for_cat += 50
            self.fullness -= 5
        elif self.house.food_for_cat < 10:
            print(COLORED.RED + f'{self.name} деньги кончились, куплю корм для кота на кредитку' + RESET)
            self.house.money -= 20
            self.house.food_for_cat += 50
            self.fullness -= 5

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Въехал в дом'.format(self.name), color='blue')

    @staticmethod
    def get_cat(_cat, house):
        _cat.go_to_the_house(house=house)

    def play_with_cat(self, _cat):
        self.fullness -= 5
        _cat.play()
        print(colorama.Fore.CYAN + f'{self.name} поиграл с {_cat.name}ом!' + RESET)

    def feed_the_cat(self, _cat):
        self.fullness -= 5
        _cat.fullness += 20
        self.house.food_for_cat -= 10
        print(COLORED.LIGHTGREEN_EX + f'{self.name} покормил кота!' + RESET)

    def act(self, _cat):
        self.fullness -= 10
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = rd.randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.dirt > 50:
            self.cleans()
        elif self.house.money < 0:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        elif dice == 3:
            self.play_with_cat(_cat)
        else:
            self.watch_mtv()
        if self.house.food_for_cat < 10:
            self.shopping()
        elif _cat.fullness <= 10:
            self.feed_the_cat(_cat)


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
        self.energy = 50
        self.name = name
        self.house = None

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}, энергии {self.energy}'

    def act(self):
        self.fullness -= 10
        self.energy -= 5
        if self.energy < 10:
            self.sleep()
        print(f'{self.name} ')

    def sleep(self):
        self.fullness -= 5
        self.energy += 30
        print(f'{self.name} поспал!')

    def play(self):
        self.fullness -= 10
        self.house.dirt += 5
        self.energy -= 10

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
for day in range(1, 100):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act(cat)
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
