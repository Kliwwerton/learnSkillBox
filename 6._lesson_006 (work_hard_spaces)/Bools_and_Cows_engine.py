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

    return numbers


def create_user_number():

    """ Create user number and return it """

    user_numbers = []
    while True:
        numbers = input('Введите четырёхзначное число: ')
        if not numbers.isdigit():
            if numbers.lower() in ('stop', 'exit'):
                break
            else:
                print('Вы ввели неверное значение, пожалуйста, попробуйте с начала!')
        elif numbers.isdigit() and len(numbers) > 4:
            print('Вы ввели более 4 чисел. Число должно состоять из четырёх цифр!')
        elif numbers.isdigit() and len(numbers) < 4:
            print('Вы ввели менее четырёх чисел. Число должно состоять из четырёх цифр!')
        elif numbers.isdigit() and int(numbers[0]) == 0:
            print('Вы ввели число, которое начинается с цифры "0", это недопустимо. Попробуйте с начала.'),
        else:
            break

    if numbers.lower() in ('stop', 'exit'):
        return numbers
    else:
        for i in numbers:
            user_numbers.append(int(i))
        # print(user_numbers)
        return user_numbers


def access_number_and_check(computer_number, user_number):

    """ Computer check the number and returns quantity Bools and Cows """

    bools_and_cows = {'bools': 0, 'cows': 0}
    for i in range(len(user_number)):
        if user_number[i] in computer_number:
            if user_number[i] == computer_number[i]:
                bools_and_cows['bools'] += 1
            else:
                bools_and_cows['cows'] += 1

    return bools_and_cows


def defines_is_win(dictionary, count):

    """ defines win or not """

    if dictionary['bools'] == 4:
        print(colorama.Fore.RED + 'Быков: ',
              dictionary['bools'], '\n'
              'Поздравляю!!! ВЫ ВЫИГРАЛИ с ', count, 'ходов.',
              colorama.Style.RESET_ALL)
        return True
    else:

        print(colorama.Fore.GREEN + 'Быков: ',
              dictionary['bools'], 'Коров: ',
              dictionary['cows'],
              colorama.Style.RESET_ALL)
        return False


def rules_of_the_game():

    """ Shows rules of the game Bools and Cows """

    print(colorama.Fore.RED + 'Правила игры в игру "Быки и Коровы":\n'
          'Компьютер загадывает четыре числа от 0 до 9, первое число не может быть 0, числа не могут повторяться.\n'
          'Игрок пытается отгадать числа. Называет четыре числа.\n'
          'Если названное число есть среди загаданных, но оно находятся не на том месте, где загадал компьютер,\n'
          'то - это "Корова", если названное число совпадает с загаданным и находится на том месте где и загадано, \n'
          'то - это "Бык".\n'
          'Игра заканчивается когда все четыре "Быка" найдены.\n'
                              'Если хотите выйти из игры, наберите команду "stop" или "exit".'
          'УДАЧИ!!!', colorama.Fore.RESET)


def is_game():
    word = 'None'
    while word.lower() not in ('да', 'yes', 'нет', 'no', 'lf', 'ytn'):
        word = input('Хотите продолжить игру? ("Да" или "Нет"): ')
        if word.isalpha():
            if word.lower() not in ('да', 'yes', 'нет', 'no', 'lf', 'ytn'):
                print('Вы ввели неверное значение!')
            continue
        else:
            print('Вы ввели неверное значение, выберите из предложенных')

    if word.title() in ('Да', 'Yes', 'Lf'):
        return True
    else:
        print('Ну как хотите, игра то интересная!')
        return False


def main():
    rules_of_the_game()
    numbers = create_numbers()
    print(numbers)


if __name__ == '__main__':
    main()
