"""
Group:
Varfolomeeva Viktoria
Sineokaya Anastasia
"""
from time import sleep
import RU_LOCAL as RU
import random

score = 0

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

def library():
    global score
    flag = 0
    print(color.BOLD + RU.library_1)
    sleep(1)
    print(color.BOLD + RU.library_2)
    sleep(1)
    print(color.BOLD + RU.library_3)
    sleep(1)
    print(color.BOLD + RU.library_4)
    sleep(1)
    print(color.BOLD + RU.library_q_1)
    sleep(1)
    print(color.BOLD + RU.library_q_2)
    sleep(1)
    ans_1 = int(input(color.BOLD + RU.library_q))
    if ans_1 == 1:
        print(color.BOLD + RU.library_q_1[2:])
        sleep(1)
        print(color.BOLD + RU.library_a_1)
        sleep(1)
        ans_2 = input(color.BOLD + RU.library_q_3).lower()
        if ans_2 == RU.library_yes:
            flag = 1
            print(color.BOLD + RU.library_q_2[2:])
            sleep(1)
            print(color.BOLD + RU.library_a_2_1)
            sleep(1)
            print(color.BOLD + RU.library_5)
            sleep(1)
            print(color.BOLD + RU.library_a_2_2)
    else:
        flag = 1
        print(color.BOLD + RU.library_q_2[2:])
        sleep(1)
        print(color.BOLD + RU.library_a_2_1)
        sleep(1)
        print(color.BOLD + RU.library_5)
        sleep(1)
        print(color.BOLD + RU.library_a_2_2)
        sleep(1)
        ans_2 = input(color.BOLD + RU.library_q_3).lower()
        if ans_2 == RU.library_yes:
            print(color.BOLD + RU.library_q_1[2:])
            sleep(1)
            print(color.BOLD + RU.library_a_1)
    print(color.BOLD + RU.library_6)
    sleep(1)
    print(color.BOLD + RU.library_7)
    sleep(1)
    if flag == 1:
        print(color.BOLD + RU.library_8)
        score += 10
    print(color.BOLD + RU.library_9, score)

library()





print(color.BOLD + RU.phrase_1)
sleep(1)
print(color.BOLD + RU.phrase_2)
sleep(1)
print(color.BOLD + RU.phrase_3)
sleep(1)
print(color.BOLD + RU.phrase_4)
sleep(1)
print(color.BOLD + RU.phrase_5)
sleep(1)
print(color.BOLD + RU.phrase_6)
sleep(4)
print(color.BOLD + RU.phrase_7)
sleep(4)
print(color.BOLD + RU.phrase_8)
sleep(4)


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