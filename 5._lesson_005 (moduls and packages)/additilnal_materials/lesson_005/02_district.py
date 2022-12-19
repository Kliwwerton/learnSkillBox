# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from district.central_street.house1.room1 import folks as dcentr_s_h_1_r_1_f
from district.central_street.house1.room2 import folks as dcentr_s_h_1_r_2_f
from district.central_street.house2.room1 import folks as dcentr_s_h_2_r_1_f
from district.central_street.house2.room2 import folks as dcentr_s_h_2_r_2_f

from district.soviet_street.house1.room1 import folks as dsovet_s_h_1_r_1_f
from district.soviet_street.house1.room2 import folks as dsovet_s_h_1_r_2_f
from district.soviet_street.house2.room1 import folks as dsovet_s_h_2_r_1_f
from district.soviet_street.house2.room2 import folks as dsovet_s_h_2_r_2_f

print('На районе живут ', ', '.join(dcentr_s_h_1_r_1_f), ', '.join(dcentr_s_h_1_r_2_f),
      ', '.join(dcentr_s_h_2_r_1_f), ', '.join(dcentr_s_h_2_r_2_f), '\n',
      ', '.join(dsovet_s_h_1_r_1_f), ', '.join(dsovet_s_h_1_r_2_f),
      ', '.join(dsovet_s_h_2_r_1_f), ', '.join(dsovet_s_h_2_r_2_f))
