# -*- coding: utf-8 -*-
import random
import colorama

_number = 0


def create_numbers():

    """ Computer create the number """

    numbers = []
    while len(numbers) < 4:
        if len(numbers) == 0:
            numbers.append(random.randint(1, 9))
        else:
            number = random.randint(0, 9)
            if number not in numbers:
                numbers.append(number)

        # print(numbers)

    return numbers


def create_user_number():

    """ Create user number and return it """

    pass


def access_number_and_check(computer_number, user_number):

    """ Computer check the number and returns quantity Bools and Cows """

    pass


def defines_is_win():

    """ defines win or not """

    pass


def rules_of_the_game():

    """ Shows rules of the game Bools and Cows """

    print(colorama.Fore.RED + 'Правила игры в игру "Быки и Коровы":\n'
          'Компьютер загадывает четыре числа от 0 до 9, первое число не может быть 0, числа не могут повторяться.\n'
          'Игрок пытается отгадать числа. Называет четыре числа.\n'
          'Если названное число есть среди загаданных, но оно находятся не на том месте, где загадал компьютер,\n'
          'то - это "Корова", если названное число совпадает с загаданным и находится на том месте где и загадано, \n'
          'то - это "Бык".\n'
          'Игра заканчивается когда все четыре "Быка" найдены.\n'
          'УДАЧИ!!!', colorama.Fore.RESET)


def is_game():
    word = 'None'
    while word.lower() not in ('да', 'yes', 'нет', 'no'):
        word = input('Хотите продолжить игру? ("Да" или "Нет"): ')
        if word.isalpha():
            continue
        else:
            print('Вы ввели неверное значение, выберите из предложенных')

    if word.title() in ('Да', 'Yes'):
        return True
    else:
        return False


def main():
    rules_of_the_game()
    numbers = create_numbers()
    print(numbers)


if __name__ == '__main__':
    main()
