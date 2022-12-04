# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
user_input_month = None
while user_input_month not in range(1, 13):
    user_input_month = int(input("Введите, пожалуйста, номер месяца: "))
    print('Вы ввели', user_input_month)
    if user_input_month not in range(1, 13):
        print('Введено неверное значение! Попробуй снова.\n'
              'Напоминаем, в году 12 месяцев!!!')
        continue
    if user_input_month in (1, 3, 5, 7, 8, 10, 12):
        print('В этом месяце 31 день')
    elif user_input_month == 2:
        print('В этом месяце 28 дней')
    elif user_input_month in (4, 6, 9, 11):
        print('В этом месяце 30 дней')
    else:
        print('Нет такого номера месяца в году, попробуйте снова!')
