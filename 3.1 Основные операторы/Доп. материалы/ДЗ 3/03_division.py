# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37

# TODO здесь ваш код
i = 0
j = a
while j > b:
    i += 1
    j -= b
print(f'Целочисленное деление {a} на {b} даёт {i}')
print(a//b)
print(a%b)
