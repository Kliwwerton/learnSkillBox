# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000

# i = 0
# sum_for_live = 0
# while i < 10:
#     money_for_a_month = expenses - educational_grant
#     sum_for_live += money_for_a_month
#     expenses *= 1.03
#     print(expenses)
#     i += 1
# sum_for_live = round(sum_for_live, 2)
# print(f'Всего нужно попросить {round(sum_for_live, 2)} рублей у своих родителей на {i} месяцев учёбы.')

i = 0
money_for_live = 0
while i < 10:
    money_for_month = expenses - educational_grant
    money_for_live += money_for_month
    print(f' На проживание в {i+1} месяце нужно {round(expenses, 2)}, стипендия'
          f' {educational_grant}, нужно попросить:'
          f' {round(money_for_month, 2)} всего на'
          f' {i+1} месяцев нужно'
          f' {round(money_for_live, 2)} плюс стипендия.')
    expenses *= 1.03
    i += 1
print(f'Всего нужно попросить {round(money_for_live, 2)} рублей у своих родителей на {i} месяцев учёбы.')
