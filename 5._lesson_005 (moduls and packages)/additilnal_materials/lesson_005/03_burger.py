# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления ингредиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью функций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает ингредиентов - создать соответствующие функции в модуле my_burger

import my_burger as mb

mb.add_a_bun()
mb.add_a_cheese()
mb.add_the_cutlet()
mb.add_a_cheese()
mb.add_the_cutlet()
mb.add_a_tomato()
mb.add_a_cheese()
mb.add_a_bun()
print('Всё, двойной чизбургер готов!')
