# -*- coding: utf-8 -*-

# Игра «Быки и коровы»

import random


def create_number():
    """Создаёт и возвращает четырёхзначное число В ВИДЕ СТРОКИ для отгадывания"""
    hidden_number = ""
    number_func = 0
    while len(hidden_number) != 4:
        if number_func == 0:
            num = random.randint(1, 9)
            hidden_number += str(num)
            number_func += 1
        else:
            num = random.randint(0, 9)
            if str(num) in hidden_number:
                continue
            else:
                hidden_number += str(num)

    return hidden_number


def request_number():
    """Запрашивает четырёхзначное число от пользователя.
    Проверяет, правильно ли введено число (нет повторяющихся знаков).
    Возвращает число, если оно введено верно."""
    number = None
    numbers = []
    while not isinstance(number, int):
        number = 0
        try:
            while len(numbers) != 4:
                number = input("Введите четырёхзначное число: ")
                for i in number:
                    numbers.append(i)
                if str(number) in ('Выход', 'выход', 'Exit', 'exit'):
                    # numbers = ['1', '1', '1', '1']
                    number = 1111
                    break
                number = int(number)
                if numbers[0] == '0':
                    print('Вы ввели число, начинающееся с "0", \n'
                          'Пожалуйста, введите четырёхзначное число, начинающееся не с "0"')
                    numbers = []
                elif len(numbers) < 4:
                    print('Вы ввели слишком короткое число!')
                elif len(numbers) > 4:
                    print('Вы ввели слишком длинное число!')
                else:
                    for i in numbers:
                        count = numbers.count(i)
                        if count > 1:
                            print('Вы ввели число с повторяющимися символами, а это противоречит нашим правилам. \n'
                                  'Пожалуйста, введите число без повторяющихся символов!')
                            numbers = []

        except ValueError:
            print('Вы ввели не число, попробуйте снова.')
            numbers = []
    return number


def check_number(hidden_number, number):
    """ Сравнивает два четырёхзначных числа, выявляет совпадения и возвращает количество "коров" и "быков" """

    results = {'bulls': 0, 'cows': 0}
    for i in hidden_number:
        if i in number:
            if hidden_number.index(i) == number.index(i):
                results['bulls'] += 1
            else:
                results['cows'] += 1
    return results
