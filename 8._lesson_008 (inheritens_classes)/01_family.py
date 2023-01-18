# -*- coding: utf-8 -*-
import random

import colorama

COLORED_font = colorama.Fore
COLORED_background = colorama.Back
RESET = colorama.Style.RESET_ALL


# ЧАСТЬ ПЕРВАЯ.
#
# Создать модель жизни небольшой семьи
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.


class Human:
    """Class Human"""

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 30
        self.happiness = 100

    def __str__(self):
        return f'{self.name}, сытость {self.fullness}, уровень счастья {self.happiness}'

    def eat(self):
        if self.house.food >= 30:
            self.fullness += 30
            self.house.food -= 30
            print(COLORED_font.LIGHTGREEN_EX + f'{self.name} покушал(а)' + RESET)
        elif 0 < self.house.food < 30:
            self.fullness += self.house.food
            self.house.food = 0
            print(COLORED_font.LIGHTGREEN_EX + f'{self.name} покушал(а)' + RESET,
                  COLORED_background.RED + 'ЕДА КОНЧИЛАСЬ' + RESET)
        else:
            print(COLORED_font.RED + f'{self.name} остался(лась) голодом!!! ЕДЫ НЕТ!!!' + RESET)

    def leaving_into_house(self, house):
        self.house = house
        self.house.residents.append(self)
        self.fullness -= 10
        print(COLORED_font.BLUE + f'{self.name}, въехал(а) в {self.house.name}' + RESET)


class House:
    total_money = 0
    total_food = 0
    total_fur_coat = 0
    total_cat_food = 0

    def __init__(self, name):
        self.name = name
        self.money = 100
        self.food = 50
        self.cat_food = 50
        self.dirt = 0
        self.house_situation = True
        self.crash = 0
        self.residents = []

    @staticmethod
    def my_residents(arg: list) -> str:
        string = ''
        if len(arg) == 1:
            string += arg[0].name
        elif len(arg) > 1:
            for j in range(len(arg) - 2):
                string += arg[j].name + ', '
            string += arg[-2].name + ' и ' + arg[-1].name
        else:
            string += 'НИКТО ЗДЕСЬ НЕ ЖИВЁТ!'
        return string

    def __str__(self):
        str_1 = self.my_residents(self.residents)
        return f'Я {self.name}, здесь живут: {str_1}\n' \
               f'Еды в холодильнике {self.food}, корма для кошек {self.cat_food}, ' \
               f'денег в тумбочке {self.money}, грязи {self.dirt}'

    def act(self):
        self.dirt += 5
        for k in self.residents:
            if k.fullness <= 0:
                print(COLORED_font.RED + f'{k.name} УМЕР(ЛА) ОТ ГОЛОДА!!!' + RESET)
                self.residents.remove(k)
            elif k.happiness < 10:
                print(COLORED_font.RED + f'{k.name} УМЕР(ЛА) ОТ ДИПРЕССИИ!!!' + RESET)
                self.residents.remove(k)
            else:
                k.act()


class Husband(Human):

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.house.house_situation:
            if self.fullness <= 30:
                self.eat()
            elif self.house.money < 100:
                self.work()
            else:
                dice = random.randint(1, 6)
                if dice == 1:
                    self.work()
                elif dice == 2:
                    if self.fullness < 100:
                        self.eat()
                    else:
                        print(COLORED_font.LIGHTWHITE_EX + f'{self.name} сыт по горло!')
                        self.gaming()
                else:
                    self.gaming()
        else:
            if self.fullness < 20:
                self.eat()
            else:
                print(COLORED_font.LIGHTBLUE_EX + f'Жена депрессует!!!')
                self.work()

    def work(self):
        self.fullness -= 10
        self.house.money += 150
        self.house.total_money += 150
        self.happiness -= 10
        print(COLORED_font.YELLOW + f'{self.name} сходил на работу!' + RESET)

    def gaming(self):
        self.fullness -= 10
        if self.happiness < 100:
            self.happiness += 20
            if self.happiness > 100:
                self.happiness = 100
        print(COLORED_font.CYAN + f'{self.name} играл в WoT целый день!' + RESET)


class Wife(Human):

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.happiness <= 30 or self.house.money < 30:
            self.house.house_situation = False
            if any(isinstance(x, Husband) for x in self.house.residents):
                print(COLORED_font.RED + f'{self.name} пилит мужа из-за наступающей депрессии!' + RESET)
        else:
            self.house.house_situation = True

        if self.fullness < 30:
            self.eat()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.cat_food < 20:
            self.cat_food_shopping()
        elif self.house.dirt >= 90:
            self.clean_house()
        elif self.house.money > 350 and self.happiness <= 30:
            self.buy_fur_coat()
        else:
            dice = random.randint(1, 2)
            if dice == 1:
                if self.fullness < 100:
                    self.eat()
                else:
                    print(COLORED_font.YELLOW + f'{self.name} сыта по горло! Пойду посплю.' + RESET)
                    self.fullness -= 10
            else:
                self.clean_house()

    def shopping(self):
        if self.house.money >= 100:
            self.house.food += 100
            self.house.total_food += 100
            self.house.money -= 100
            self.happiness += 20
            self.fullness -= 10
            print(COLORED_font.MAGENTA + f'{self.name} сходила за покупками!' + RESET)
        elif self.house.money < 100:
            self.house.food += self.house.money
            self.house.total_food += self.house.money
            self.house.money = 0
            self.fullness -= 10
            self.happiness += 10
            print(COLORED_font.MAGENTA + f'{self.name} сходила за покупками!' + RESET)
        else:
            print(COLORED_font.RED + f'Денег нет, но вы держитесь! {self.name} '
                                     f'не купила еды, потому что раздолбай муж их не заработал!!!')

    def cat_food_shopping(self):
        if self.house.money < 30:
            print(COLORED_font.RED + f'Нет денег на корм для кота!' + RESET)
        else:
            self.house.money -= 30
            self.house.cat_food += 30
            self.fullness -= 10
            self.happiness += 5
            self.house.total_cat_food += 30
            print(COLORED_font.BLUE + f'{self.name} сходила за кормом для кота.' + RESET)

    def buy_fur_coat(self):
        self.happiness += 60
        self.house.money -= 350
        self.fullness -= 10
        self.house.total_fur_coat += 1
        print(COLORED_font.GREEN + f'{self.name} купила себе новую шубу!' + RESET)

    def clean_house(self):
        self.house.dirt -= 100
        if self.house.dirt <= 0:
            self.house.dirt = 0
        self.fullness -= 10
        self.happiness -= 10
        print(COLORED_font.LIGHTRED_EX + f'{self.name} прибралась в доме!' + RESET)


# home = House(name='Домик')
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# serge.leaving_into_house(house=home)
# masha.leaving_into_house(house=home)
#
# for day in range(365):
#     print('================== День {} =================='.format(day))
#     home.act()
#     for i in home.residents:
#         print(i)
#
#     print(home)
#
# print(COLORED_font.RED + f'============================ ИТОГИ ГОДА! ==========================')
# print(COLORED_font.LIGHTCYAN_EX + 'Всего за год купили: ', home.total_food, 'еды',
#       '\nЗаработано: ', home.total_money, 'денег, '
#       '\nКуплено: ', home.total_fur_coat, 'шуб' + RESET)


# ЧАСТЬ ВТОРАЯ
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self, name):
        self.name = name
        self.house = None
        self.fullness = 50
        self.happiness = 100

    def __str__(self):
        return f'{self.name}, сытость {self.fullness}'

    def act(self):
        self.happiness -= 10
        self.house.dirt += 5
        if self.fullness <= 20:
            self.eat()
        elif self.happiness < 30:
            self.soil()
        else:
            self.sleep()

    def eat(self):
        self.house.dirt += 5
        if self.house.cat_food >= 30:
            self.fullness += 30
            self.house.cat_food -= 30
            print(COLORED_font.CYAN + f'{self.name} покушал(а)' + RESET)
        elif 30 > self.house.cat_food > 0:
            self.fullness += self.house.cat_food
            self.house.cat_food = 0
            print(COLORED_font.CYAN + f'{self.name} покушал(а), но не досыта!!!' + RESET)
        else:
            print(COLORED_font.RED + f'{self.name} остался(лась) голодом, КОРМА НЕТ!')

    def sleep(self):
        self.fullness -= 10
        print(COLORED_font.LIGHTGREEN_EX + f'{self.name} поспал!' + RESET)

    def soil(self):
        self.fullness -= 10
        self.happiness += 50
        self.house.dirt += 50
        self.house.crash += 10
        print(COLORED_font.BLUE + f"{self.name} ДРАЛ ОБОИ!!!" + RESET)

    def leaving_into_house(self, house):
        self.house = house
        self.fullness -= 10
        self.house.residents.append(self)
        print(COLORED_font.RED + f'{self.name} теперь живёт в {self.house.name}')


# ЧАСТЬ ВТОРАЯ БИС
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


#  ЧАСТЬ ТРЕТЬЯ
#
# после подтверждения учителем второй части (обеих веток)
# влить в ветку мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House('Домик')
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
# kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')
serge.leaving_into_house(house=home)
masha.leaving_into_house(house=home)
murzik.leaving_into_house(house=home)

for day in range(365):
    print('================== День {} =================='.format(day))
    home.act()
    for i in home.residents:
        print(i)

    print(home)

print(COLORED_font.LIGHTCYAN_EX + 'Всего за год купили: ', home.total_food, 'еды',
      '\nКорма для кошек: ', home.total_cat_food,
      '\nЗаработано: ', home.total_money, 'денег, '
      '\nКуплено: ', home.total_fur_coat, 'шуб' + RESET)

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживания случайностей моделирование за год делать 3 раза, если 2 из 3‑х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
