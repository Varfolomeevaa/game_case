"""
Group:
Varfolomeeva Viktoria
Sineokaya Anastasia
"""

from time import sleep

import RU_LOCAL as RU
import random

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print(color.BOLD + RU.phrase1)

k = 0
b = []
print(k)
c = ''
while k != 4:
    if 'сходить в библиотеку' in b:
        c = '-сходить в аптеку'
    print('''Вы можете…
-сходить в библиотеку
-сходить в кинотеатр
-сходить в университет''')
    print(c)
    a = input('Ваш выбор:')
    if a in b:
        print('Вы там уже были! Выберете другую локацию')
    else:
        if a == 'сходить в библиотеку':
            k += 1
            b.append(a)
            print('да1')
        elif a == 'сходить в кинотеатр':
            k += 1
            b.append(a)
            print('да2')
        elif a == 'сходить в университет':
            k += 1
            b.append(a)
            print('да3')
        elif a == 'сходить в аптеку':
            k += 1
            b.append(a)
            print('да4')