# -*- coding: utf-8 -*-
import random as rd

import colorama

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
            print(COLORED.LIGHTWHITE_EX + f'{self.name} поел' + RESET)
            self.fullness += 30
            if self.fullness >= 100:
                self.fullness = 100
            self.house.food -= 10
        else:
            print(COLORED.CYAN + f'{self.name} нет еды' + RESET)

    def cleans(self):
        print(COLORED.LIGHTBLUE_EX + f'{self.name} прибрался в доме!' + RESET)
        self.fullness -= 10
        self.house.dirt = 0

    def work(self):
        print(COLORED.YELLOW + f'{self.name} сходил на работу' + RESET)
        self.house.money += 50
        self.fullness -= 20

    def watch_mtv(self):
        print(COLORED.BLUE + f'{self.name} смотрел MTV целый день' + RESET)
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
        self.house.residents_people.append(self)
        print(f'{self.name} Въехал в дом')

    def left_to_the_house(self):
        self.house = None
        print(f'{self.name} выехал из дома!')

    @staticmethod
    def get_cat(_cat, house):
        _cat.go_to_the_house(house=house)

    def play_with_cat(self, _cat):
        self.fullness -= 5
        _cat.play_with_owner()
        print(COLORED.CYAN + f'{self.name} поиграл с {_cat.name}ом!' + RESET)

    def feed_the_cat(self, _cat):
        self.fullness -= 5
        _cat.fullness += 30
        self.house.food_for_cat -= 10
        print(COLORED.LIGHTGREEN_EX + f'{self.name} покормил кота!' + RESET)

    def act(self, _cat):

        if self.fullness <= 0:
            print(COLORED.BLUE + f'{self.name} умер...' + RESET)
            self.left_to_the_house()
            return
        if self.house:
            dice = rd.randint(1, 6)
            if self.fullness < 30:
                self.eat()
            elif self.house.food < 10:
                self.shopping()
            elif self.house.dirt > 80:
                self.cleans()
            elif self.house.money < 0:
                self.work()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            elif dice == 3:
                self.play_with_cat(_cat)
            elif dice == 4:
                self.cleans()
            else:
                self.watch_mtv()

            if self.house.food_for_cat < 10:
                self.shopping()
            elif _cat.fullness <= 20:
                self.feed_the_cat(_cat)
        else:
            return


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.food_for_cat = 0
        self.dirt = 0
        self.residents_people = []
        self.residents_cats = []

    def __str__(self):
        if self.residents_people and self.residents_cats:
            return f'В доме еды {self.food}, корма {self.food_for_cat}, денег {self.money}, грязи {self.dirt}\n' \
                   f'В доме сейчас живут Люди: {[j.name for j in self.residents_people]} ' \
                   f'И кошки: {[k.name for k in self.residents_cats]}'
        else:
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
        self.action = True

    def __str__(self):
        return f'Я {self.name}, сытость {self.fullness}, энергии {self.energy}'

    def act(self):
        if self.fullness <= 0:
            print(COLORED.RED + f'{self.name} ПОДОХ от ГОЛОДА!!!' + RESET)
            return
        self.fullness -= 5
        self.energy -= 5
        dice = rd.randint(1, 6)
        if self.energy < 10:
            self.sleep()

        elif self.action:
            if dice == 1:
                self.play()
            elif dice == 2:
                self.scratching_the_wallpaper()
            elif dice == 3:
                self.shat()
            elif self.energy > 80:
                self.scratching_the_wallpaper()
            else:
                self.sleep()
        else:
            self.action = True

    def sleep(self):
        self.fullness -= 5
        self.energy += 30
        print(f'{self.name} поспал!')

    def play(self):
        self.fullness -= 10
        self.house.dirt += 5
        self.energy -= 10

        print(COLORED.YELLOW + f'{self.name} поиграл с ТРИКСИ' + RESET)

    def play_with_owner(self):
        self.fullness -= 10
        self.house.dirt += 5
        self.energy -= 10
        self.action = False
        print(COLORED.LIGHTCYAN_EX + f'{self.name} поиграл с хозяином!' + RESET)

    def scratching_the_wallpaper(self):
        self.fullness -= 10
        self.energy -= 10
        self.house.dirt += 20
        print(COLORED.MAGENTA + f'{self.name} ДРАЛ ОБОИ!!!' + RESET)

    def shat(self):
        self.fullness -= 5
        self.house.dirt += 30
        self.energy -= 10
        print(COLORED.LIGHTGREEN_EX + f'{self.name} нагадил в угол!' + RESET)

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        self.energy -= 10
        self.house.residents_cats.append(self)
        print(colorama.Fore.RED + f'{self.name} поселился в доме!', colorama.Style.RESET_ALL)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    # Man(name='Кенни'),
]
cat = Cat(name='Мурзик')
my_sweet_home = House()
for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)
citizens[0].get_cat(_cat=cat, house=my_sweet_home)
print(my_sweet_home)
for day in range(1, 100):
    print('================ день {} =================='.format(day))
    for i in my_sweet_home.residents_people:
        i.act(cat)

    cat.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    print(cat)
    my_sweet_home.check()

    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
