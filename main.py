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
    print('')
    sleep(1)
    print(color.BOLD + RU.library_2)
    sleep(1)
    print(color.BOLD + RU.library_3)
    sleep(1)
    print('')
    print(color.BOLD + RU.library_4)
    print('')
    sleep(1)
    ans_1 = int(input(color.BOLD + RU.library_q))
    print('')
    if ans_1 == 1:
        print(color.BOLD + RU.library_q_1)
        sleep(1)
        print(color.BOLD + RU.library_a_1)
        sleep(1)
        print('')
        ans_2 = int(input(color.BOLD + RU.library_q_3))
        print('')
        if ans_2 == 1:
            print(color.BOLD + RU.library_q_2)
            sleep(1)
            print(color.BOLD + RU.library_a_2_1)
            sleep(1)
            rand = random.randint(0,1)
            if rand == 1:
                print(color.BOLD + RU.library_random_1)
                sleep(1)
                print('')
                print(color.BOLD + RU.library_random_2)
                print('')
                sleep(1)
                print(color.BOLD + RU.library_random_3)
                flag = 1
            print(color.BOLD + RU.library_a_2_2)
    else:
        print(color.BOLD + RU.library_q_2)
        sleep(1)
        print(color.BOLD + RU.library_a_2_1)
        rand = random.randint(0, 1)
        if rand == 1:
            print(color.BOLD + RU.library_random_1)
            sleep(1)
            print('')
            print(color.BOLD + RU.library_random_2)
            print('')
            sleep(1)
            print(color.BOLD + RU.library_random_3)
            flag = 1
        print(color.BOLD + RU.library_a_2_2)
        print('')
        ans_2 = int(input(color.BOLD + RU.library_q_3))
        print('')
        if ans_2 == 1:
            print(color.BOLD + RU.library_q_1)
            sleep(1)
            print(color.BOLD + RU.library_a_1)
    print(color.BOLD + RU.library_6)
    sleep(1)
    print(color.BOLD + RU.library_7)
    sleep(1)
    print('')
    print(color.BOLD + RU.library_8)
    if flag == 1:
        score += 10


def pharmacy():
   global score
   flag = 0
   print(color.BOLD + RU.pharmacy_1)
   print('')
   sleep(2)
   print(color.BOLD + RU.pharmacy_2)
   sleep(2)
   print(color.BOLD + RU.pharmacy_3)
   sleep(2)
   print(color.BOLD + RU.pharmacy_4)
   sleep(2)
   print('')
   ans_1 = int(input(color.BOLD + RU.pharmacy_q_1_1))
   print('')
   if ans_1 == 1:
      print(color.BOLD + RU.pharmacy_q_1)
      sleep(2)
      print(color.BOLD + RU.pharmacy_a_1)
      sleep(2)
      print('')
      ans_2 = int(input(color.BOLD + RU.pharmacy_q_1_2))
      print('')
      if ans_2 == 1:
         print(color.BOLD + RU.pharmacy_q_2)
         sleep(2)
         print(color.BOLD + RU.pharmacy_a_2)
      elif ans_2 == 2:
         flag = 1
         print(color.BOLD + RU.pharmacy_q_2_1)
         sleep(2)
         print(color.BOLD + RU.pharmacy_q_2_2)
         sleep(2)
         print(color.BOLD + RU.pharmacy_a_3)
   elif ans_1 == 2:
      print(color.BOLD + RU.pharmacy_q_2)
      sleep(2)
      print(color.BOLD + RU.pharmacy_a_2)
      print('')
      ans_2 = int(input(color.BOLD + RU.pharmacy_q_3))
      print('')
      if ans_2 == 1:
         print(color.BOLD + RU.pharmacy_q_1)
         sleep(2)
         print(color.BOLD + RU.pharmacy_a_1)
         sleep(2)
         print('')
         ans_3 = int(input(color.BOLD + RU.pharmacy_q_4))
         print('')
         if ans_3 == 1:
            flag = 1
            print(color.BOLD + RU.pharmacy_q_2_1)
            sleep(2)
            print(color.BOLD + RU.pharmacy_q_2_2)
            sleep(2)
            print(color.BOLD + RU.pharmacy_a_3)
   print(color.BOLD + RU.pharmacy_5)
   sleep(2)
   print(color.BOLD + RU.pharmacy_6)
   if flag == 1:
      score += 10
   print('')
   print(color.BOLD + RU.pharmacy_7)

def talk():
   print(color.BOLD + RU.talk_1)
   sleep(2)
   print('')
   print(color.BOLD + RU.talk_2)
   sleep(2)
   print(color.BOLD + RU.talk_3)
   sleep(2)
   print(color.BOLD + RU.talk_4)
   sleep(2)
   print(color.BOLD + RU.talk_5)
   sleep(2)
   print(color.BOLD + RU.talk_6)

def cinema():

    print(color.BOLD + RU.cinema_1)
    sleep(1)
    print(color.BOLD + RU.cinema_2)
    sleep(1.5)
    print(color.BOLD + RU.cinema_3)
    sleep(1.5)
    print(color.BOLD + RU.cinema_4)
    ans1 = int(input(RU.cinema_4_1))

    if ans1 == 1:
        print(color.BOLD + RU.cinema_5)
        sleep(1.5)
        print(color.BOLD + RU.cinema_6)
        sleep(1.5)
        print(color.BOLD + RU.cinema_6_1)
        sleep(1)
        print(color.BOLD + RU.cinema_7)
        ans2 = int(input(color.BOLD + RU.cinema_8))
        if ans2 == 1:
            print(color.BOLD + RU.cinema_9)
            a = r.randint(0, 1)
            if a == 1:
                print(color.BOLD + RU.cinema_14)
                sleep(1)
                print(color.BOLD + RU.cinema_15)
                sleep(1)
                print(color.BOLD + RU.cinema_12)
                sleep(1)
                print(color.BOLD + RU.cinema_13)
                score += 10
            elif a == 0:
                print(color.BOLD + RU.cinema_16)
                sleep(1.5)
                print(color.BOLD + RU.cinema_17)
                sleep(1.5)
                print(color.BOLD + RU.cinema_18)
        elif ans2 == 2:
            print(color.BOLD + RU.cinema_12)
            sleep(1)
            print(color.BOLD + RU.cinema_13)
    elif ans1 == 2:
        print(color.BOLD + RU.cinema_9)
        a = r.randint(0, 1)
        if a == 1:
            print(color.BOLD + RU.cinema_14)
            sleep(1)
            print(color.BOLD + RU.cinema_15)
            sleep(1)
            print(color.BOLD + RU.cinema_12)
            sleep(1)
            print(color.BOLD + RU.cinema_13)
            score += 10
        elif a == 0:
            print(color.BOLD + RU.cinema_16)
            sleep(1.5)
            print(color.BOLD + RU.cinema_17)
            sleep(1.5)
            print(color.BOLD + RU.cinema_18)

    print(color.BOLD + RU.cinema_19)

def university():
   global score
   print(color.BOLD + RU.university_1)
   sleep(2)
   print(color.BOLD + RU.university_2)
   sleep(2)
   ans1 = int(input(color.BOLD + RU.university_3))
   print(color.BOLD + RU.university_4)
   sleep(2)
   print(color.BOLD + RU.university_5)
   sleep(2)
   print(color.BOLD + RU.university_6)
   ans2 = int(input(color.BOLD + RU.university_3))
   if ans2 == 1:
      print(color.BOLD + RU.university_7)
      sleep(1.5)
      print(color.BOLD + RU.university_8)
      ans3 = int(input(color.BOLD + RU.university_9))
      if ans3 == 1:
         print(color.BOLD + RU.university_10)
         sleep(1.5)
         print(color.BOLD + RU.university_11)
         sleep(1.5)
         print(color.BOLD + RU.university_12)
         sleep(1.5)
         print(color.BOLD + RU.university_13)
      elif ans3 == 2:
         print(color.BOLD + RU.university_12)
         sleep(1.5)
         print(color.BOLD + RU.university_13)
   elif ans2 == 2:
      print(color.BOLD + RU.university_10)
      sleep(1.5)
      print(color.BOLD + RU.university_11)
      ans3 = int(input(color.BOLD + RU.university_9))
      if ans3 == 1:
         print(color.BOLD + RU.university_7)
         sleep(1.5)
         print(color.BOLD + RU.university_8)
         sleep(1.5)
         print(color.BOLD + RU.university_12)
         sleep(1.5)
         print(color.BOLD + RU.university_13)
      elif ans3 == 2:
         print(color.BOLD + RU.university_12)
         sleep(1.5)
         print(color.BOLD + RU.university_13)

   print((color.BOLD + RU.university_14))

   if ans1 == 2:
      print(color.BOLD + RU.university_15)
   elif ans1 == 1:
      print(color.BOLD + RU.university_16)
      sleep(1.5)
      print(color.BOLD + RU.university_17)
      sleep(1.5)
      print(color.BOLD + RU.university_18)
      sleep(1.5)
      print(color.BOLD + RU.university_19)
      sleep(1.5)
      print(color.BOLD + RU.university_20)
      sleep(1.5)
      print(color.BOLD + RU.university_21)
      sleep(1.5)
      print(color.BOLD + RU.university_22)
      sleep(1.5)
      print(color.BOLD + RU.university_23)
      sleep(1.5)
      print(color.BOLD + RU.university_24)
      sleep(1.5)
      print(color.BOLD + RU.university_25)
      sleep(1.5)
      score += 10

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