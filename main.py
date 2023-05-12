"""
Group:
Varfolomeeva Viktoria
Sineokaya Anastasia
"""

from time import sleep
import RU_LOCAL as ru
import random
k = 0
b = []
print(b)
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