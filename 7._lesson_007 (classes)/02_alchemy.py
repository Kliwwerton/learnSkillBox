# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля,   Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __add__(self, other):
        if isinstance(other, (Air, Fire, Earth)):
            if other == Fire:
                return Storm()

    def __str__(self):
        return 'Вода'


class Air:

    def __add__(self, other):
        pass


class Fire:

    def __add__(self, other):
        if isinstance(other, (Water, Air, Earth)):
            if other == Water:
                return Storm()
        else:
            print("Не относится ни к одному из классов!")

    def __str__(self):
        return 'Огонь'


class Earth:

    def __add__(self, other):
        pass


class Storm:
    title = 'Шторм'

    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


def main():
    water = Water()
    earth = Earth()
    fire = Fire()
    air = Air()
    # storm = Storm()
    iq1 = water + fire
    print(iq1)


if __name__ == '__main__':
    main()


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
