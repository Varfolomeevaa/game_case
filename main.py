"""
Group:
Varfolomeeva Viktoria 60
Sineokaya Anastasia
"""
from time import sleep
import RU_LOCAL as RU
import random

score = 0
evidence = []
flag_1 = 0
flag_2 = 0


class COLOR:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def library():
    global score
    print(COLOR.BOLD + RU.library_1)
    print('')
    sleep(1.2)
    print(COLOR.BOLD + RU.library_2)
    sleep(2.3)
    print(COLOR.BOLD + RU.library_3)
    sleep(6.2)
    print(COLOR.BOLD + RU.library_4)
    sleep(5.3)
    print(COLOR.BOLD + RU.library_q_2)
    sleep(5.4)
    print(COLOR.BOLD + RU.library_a_2_1)
    sleep(16.5)
    print('')
    print(COLOR.BOLD + RU.library_10)
    print('')
    sleep(2.2)
    print(COLOR.BOLD + RU.library_a_2_2)
    sleep(13)
    print('')
    ans = int(input(COLOR.BOLD + RU.library_q))
    print('')
    if ans == 1:
        print(COLOR.BOLD + RU.library_q_1)
        sleep(2.5)
        print(COLOR.BOLD + RU.library_a_1)
        sleep(19)
    print(COLOR.BOLD + RU.library_6)
    sleep(3)
    print(COLOR.BOLD + RU.library_7)
    sleep(1.5)
    print('')
    print(COLOR.BOLD + RU.library_8)
    sleep(2)
    score += 20
    evidence.append(RU.library_11)
    evidence.append(RU.library_9)


def pharmacy():
    global score
    global flag_2
    flag = 0
    print(COLOR.BOLD + RU.pharmacy_1)
    print('')
    sleep(1)
    print(COLOR.BOLD + RU.pharmacy_2)
    sleep(1.2)
    print(COLOR.BOLD + RU.pharmacy_3)
    sleep(1.2)
    print(COLOR.BOLD + RU.pharmacy_4)
    sleep(6.3)
    print('')
    ans_1 = int(input(COLOR.BOLD + RU.pharmacy_q_1_1))
    print('')
    if ans_1 == 1:
        print(COLOR.BOLD + RU.pharmacy_q_1)
        sleep(4.2)
        print(COLOR.BOLD + RU.pharmacy_a_1)
        sleep(9)
        print('')
        ans_2 = int(input(COLOR.BOLD + RU.pharmacy_q_1_2))
        print('')
        if ans_2 == 1:
            print(COLOR.BOLD + RU.pharmacy_q_2)
            sleep(4.3)
            print(COLOR.BOLD + RU.pharmacy_a_2)
            sleep(6.2)
        elif ans_2 == 2:
            flag = 1
            flag_2 = 1
            print(COLOR.BOLD + RU.pharmacy_q_2_1)
            sleep(2.1)
            print(COLOR.BOLD + RU.pharmacy_q_2_2)
            sleep(8.4)
            print(COLOR.BOLD + RU.pharmacy_a_3)
            sleep(7.3)
    elif ans_1 == 2:
        print(COLOR.BOLD + RU.pharmacy_q_2)
        sleep(4.3)
        print(COLOR.BOLD + RU.pharmacy_a_2)
        sleep(6.2)
        print('')
        ans_2 = int(input(COLOR.BOLD + RU.pharmacy_q_3))
        print('')
        if ans_2 == 1:
            print(COLOR.BOLD + RU.pharmacy_q_1)
            sleep(4.2)
            print(COLOR.BOLD + RU.pharmacy_a_1)
            sleep(9)
            print('')
            ans_3 = int(input(COLOR.BOLD + RU.pharmacy_q_4))
            print('')
            if ans_3 == 1:
                flag = 1
                flag_2 = 1
                print(COLOR.BOLD + RU.pharmacy_q_2_1)
                sleep(2.1)
                print(COLOR.BOLD + RU.pharmacy_q_2_2)
                sleep(8.4)
                print(COLOR.BOLD + RU.pharmacy_a_3)
                sleep(7.3)
    print(COLOR.BOLD + RU.pharmacy_5)
    sleep(1)
    print(COLOR.BOLD + RU.pharmacy_6)
    sleep(1)
    if flag == 1:
        score += 10
        evidence.append(RU.pharmacy_8)
    print('')
    print(COLOR.BOLD + RU.pharmacy_7)
    sleep(1)


def talk():
    print(COLOR.BOLD + RU.talk_1)
    sleep(1.2)
    print('')
    print(COLOR.BOLD + RU.talk_2)
    sleep(2.4)
    print(COLOR.BOLD + RU.talk_3)
    sleep(2.4)
    print(COLOR.BOLD + RU.talk_4)
    sleep(2.1)
    print(COLOR.BOLD + RU.talk_5)
    sleep(2.1)
    print(COLOR.BOLD + RU.talk_6)
    sleep(1)


def call():
    global score
    print(COLOR.BOLD + RU.call_1)
    print('')
    sleep(1)
    print(COLOR.BOLD + RU.call_2)
    sleep(1)
    print(COLOR.BOLD + RU.call_3)
    sleep(5)
    print(COLOR.BOLD + RU.call_4)
    sleep(1.4)
    print(COLOR.BOLD + RU.call_5)
    sleep(14)
    print(COLOR.BOLD + RU.call_6)
    sleep(2.4)
    print(COLOR.BOLD + RU.call_7)
    sleep(3)
    print(COLOR.BOLD + RU.call_8)
    sleep(2.3)
    print(COLOR.BOLD + RU.call_9)
    sleep(1)
    score += 10
    evidence.append(RU.call_10)


def letter():
    global score
    global flag_2
    if flag_2 == 0:
        print(COLOR.BOLD + RU.letter_1)
        sleep(2.3)
        print('')
        print(COLOR.BOLD + RU.letter_2)
        score += 5
        evidence.append(RU.letter_3)
        sleep(3)


def evid():
    global score
    print(COLOR.BOLD + RU.evid_1)
    print(*evidence, sep=';')
    sleep(3)
    print(COLOR.BOLD + RU.evid_2)
    if score >= 40 or RU.cap in evidence or RU.camera in evidence:
        print(COLOR.BOLD + RU.evid_3)
        sleep(3)
        examination()
    else:
        print(COLOR.BOLD + RU.evid_4)
        sleep(3)
        interrogation()


def examination():
    print(COLOR.BOLD + RU.examination_1)
    sleep(1.3)
    print(COLOR.BOLD + RU.examination_2)
    sleep(1)
    print(COLOR.BOLD + RU.examination_3)
    sleep(8)
    print(COLOR.BOLD + RU.examination_4)
    sleep(1)
    print(COLOR.BOLD + RU.examination_5)
    sleep(4)
    print(COLOR.BOLD + RU.examination_6)
    sleep(1)
    ans = int(input(COLOR.BOLD + RU.interrogation_20))
    if ans == 1:
        print(COLOR.BOLD + RU.story)
    print(COLOR.BOLD + RU.conclusion)
    sleep(1.5)


def cinema():
    global score
    global flag_1
    print(COLOR.BOLD + RU.cinema_1)
    sleep(3.5)
    print(COLOR.BOLD + RU.cinema_2)
    sleep(3.5)
    print(COLOR.BOLD + RU.cinema_3)
    sleep(7)
    print(COLOR.BOLD + RU.cinema_4)
    ans1 = int(input(RU.cinema_4_1))

    if ans1 == 1:
        print(COLOR.BOLD + RU.cinema_5)
        sleep(4.3)
        print(COLOR.BOLD + RU.cinema_6)
        sleep(12)
        print(COLOR.BOLD + RU.cinema_6_1)
        sleep(7.8)
        print(COLOR.BOLD + RU.cinema_7)
        ans2 = int(input(COLOR.BOLD + RU.cinema_8))
        if ans2 == 1:
            print(COLOR.BOLD + RU.cinema_9)
            sleep(3)
            a = random.randint(0, 1)
            if a == 1:
                print(COLOR.BOLD + RU.cinema_14)
                sleep(1)
                print(COLOR.BOLD + RU.cinema_15)
                sleep(1)
                print(COLOR.BOLD + RU.cinema_12)
                sleep(1)
                print(COLOR.BOLD + RU.cinema_13)
                sleep(2)
                score += 10
                flag_1 += 1
                evidence.append(RU.camera)
                print(COLOR.BOLD + RU.cinema_19)
                sleep(3)
            elif a == 0:
                print(COLOR.BOLD + RU.cinema_16)
                sleep(1.2)
                print(COLOR.BOLD + RU.cinema_17)
                sleep(1)
                print(COLOR.BOLD + RU.cinema_18)
                sleep(2)
                print(COLOR.BOLD + RU.cinema_19)
                sleep(3)
        elif ans2 == 2:
            print(COLOR.BOLD + RU.cinema_12)
            sleep(1)
            print(COLOR.BOLD + RU.cinema_13)
            sleep(1)
            print(COLOR.BOLD + RU.cinema_19)
            sleep(3)
    elif ans1 == 2:
        print(COLOR.BOLD + RU.cinema_9)
        sleep(3)
        a = random.randint(0, 1)
        if a == 1:
            print(COLOR.BOLD + RU.cinema_14)
            sleep(2)
            print(COLOR.BOLD + RU.cinema_15)
            sleep(2.9)
            score += 10
            flag_1 += 1
            evidence.append(RU.camera)
            print(COLOR.BOLD + RU.cinema_7)
            b = int(input(COLOR.BOLD + RU.cinema_8))
            if b == 1:
                print(COLOR.BOLD + RU.cinema_5)
                sleep(4.3)
                print(COLOR.BOLD + RU.cinema_6)
                sleep(12)
                print(COLOR.BOLD + RU.cinema_6_1)
                sleep(7.8)
                print(COLOR.BOLD + RU.cinema_12)
                sleep(3)
                print(COLOR.BOLD + RU.cinema_13)
                sleep(2)
                print(COLOR.BOLD + RU.cinema_19)
                sleep(3)
            else:
                print(COLOR.BOLD + RU.cinema_12)
                sleep(3)
                print(COLOR.BOLD + RU.cinema_13)
                sleep(2)
                print(COLOR.BOLD + RU.cinema_19)
                sleep(3)
        elif a == 0:
            print(COLOR.BOLD + RU.cinema_16)
            sleep(6)
            print(COLOR.BOLD + RU.cinema_7)
            b = int(input(COLOR.BOLD + RU.cinema_8))
            if b == 1:
                print(COLOR.BOLD + RU.cinema_5)
                sleep(4.3)
                print(COLOR.BOLD + RU.cinema_6)
                sleep(12)
                print(COLOR.BOLD + RU.cinema_6_1)
                sleep(7.8)
                print(COLOR.BOLD + RU.cinema_12)
                sleep(3)
                print(COLOR.BOLD + RU.cinema_13)
                sleep(2)
                print(COLOR.BOLD + RU.cinema_19)
                sleep(3)
            else:
                print(COLOR.BOLD + RU.cinema_17)
                sleep(3)
                print(COLOR.BOLD + RU.cinema_18)
                sleep(2)
                print(COLOR.BOLD + RU.cinema_19)
                sleep(3)


def university():
    global score
    print(COLOR.BOLD + RU.university_1)
    sleep(7.1)
    print(COLOR.BOLD + RU.university_2)
    ans1 = int(input(COLOR.BOLD + RU.university_3))
    print(COLOR.BOLD + RU.university_4)
    sleep(7.1)
    print(COLOR.BOLD + RU.university_5)
    sleep(3.5)
    print(COLOR.BOLD + RU.university_6)
    ans2 = int(input(COLOR.BOLD + RU.university_3))
    if ans2 == 1:
        print(COLOR.BOLD + RU.university_7)
        sleep(6.5)
        print(COLOR.BOLD + RU.university_8)
        sleep(7)
        ans3 = int(input(COLOR.BOLD + RU.university_9))
        if ans3 == 1:
            print(COLOR.BOLD + RU.university_10)
            sleep(5.3)
            print(COLOR.BOLD + RU.university_11)
            sleep(4.4)
            print(COLOR.BOLD + RU.university_12)
            sleep(3.5)
            print(COLOR.BOLD + RU.university_13)
        elif ans3 == 2:
            print(COLOR.BOLD + RU.university_12)
            sleep(3.5)
            print(COLOR.BOLD + RU.university_13)
    elif ans2 == 2:
        print(COLOR.BOLD + RU.university_10)
        sleep(5.3)
        print(COLOR.BOLD + RU.university_11)
        sleep(3.5)
        ans3 = int(input(COLOR.BOLD + RU.university_9))
        if ans3 == 1:
            print(COLOR.BOLD + RU.university_7)
            sleep(5.5)
            print(COLOR.BOLD + RU.university_8)
            sleep(6.7)
            print(COLOR.BOLD + RU.university_12)
            sleep(3.7)
            print(COLOR.BOLD + RU.university_13)
        elif ans3 == 2:
            print(COLOR.BOLD + RU.university_12)
            sleep(3.7)
            print(COLOR.BOLD + RU.university_13)

    print((COLOR.BOLD + RU.university_14))
    sleep(3)

    if ans1 == 2:
        print(COLOR.BOLD + RU.university_15)
        sleep(5.1)
        print(COLOR.BOLD + RU.university_25)
    elif ans1 == 1:
        print(COLOR.BOLD + RU.university_16)
        sleep(4.1)
        print(COLOR.BOLD + RU.university_17)
        sleep(2.4)
        print(COLOR.BOLD + RU.university_18)
        sleep(3.2)
        print(COLOR.BOLD + RU.university_19)
        sleep(2.1)
        print(COLOR.BOLD + RU.university_20)
        sleep(20)
        print(COLOR.BOLD + RU.university_21)
        sleep(3)
        print(COLOR.BOLD + RU.university_22)
        sleep(6.4)
        print(COLOR.BOLD + RU.university_23)
        sleep(7.3)
        print(COLOR.BOLD + RU.university_24)
        sleep(1.3)
        print(COLOR.BOLD + RU.university_25)
        evidence.append(RU.cap)
        score += 10


def start():
    print(COLOR.BOLD + RU.rules)
    sleep(26)
    print(COLOR.BOLD + RU.phrase_1)
    sleep(11)
    print(COLOR.BOLD + RU.phrase_2)
    sleep(1)
    print(COLOR.BOLD + RU.phrase_3)
    sleep(11)
    print(COLOR.BOLD + RU.phrase_4)
    sleep(3)
    print(COLOR.BOLD + RU.phrase_5)
    sleep(6)
    print(COLOR.BOLD + RU.phrase_6)
    sleep(20)
    print(COLOR.BOLD + RU.phrase_7)
    sleep(20)
    print(COLOR.BOLD + RU.phrase_8)
    sleep(20)


def interrogation():
    print(COLOR.BOLD + RU.interrogation_1)
    sleep(4.6)
    print(COLOR.BOLD + RU.interrogation_2)
    sleep(5)
    print(COLOR.BOLD + RU.interrogation_3)
    sleep(2.3)
    print(COLOR.BOLD + RU.interrogation_4)
    sleep(1.2)
    print(COLOR.BOLD + RU.interrogation_5)
    sleep(1.1)
    print(COLOR.BOLD + RU.interrogation_6)
    sleep(7)
    print(COLOR.BOLD + RU.interrogation_7)
    sleep(3)
    print(COLOR.BOLD + RU.interrogation_8)
    sleep(6)
    print(COLOR.BOLD + RU.interrogation_9)
    sleep(6.1)
    print(COLOR.BOLD + RU.interrogation_10)
    sleep(4.1)
    print(COLOR.BOLD + RU.interrogation_11)
    sleep(9.2)
    if flag_1 == 1:
        print(COLOR.BOLD + RU.interrogation_12)
        sleep(2.1)
        print(COLOR.BOLD + RU.interrogation_13)
        sleep(5)
    print(COLOR.BOLD + RU.interrogation_14)
    sleep(3)
    print(COLOR.BOLD + RU.interrogation_15)
    sleep(1.1)
    print(COLOR.BOLD + RU.interrogation_16)
    sleep(1)
    print(COLOR.BOLD + RU.interrogation_17)
    sleep(3.4)
    print(COLOR.BOLD + RU.interrogation_18)
    sleep(1.2)
    print(COLOR.BOLD + RU.interrogation_19)
    a = int(input(COLOR.BOLD + RU.interrogation_19_1))
    if a == 2:
        print(COLOR.BOLD + RU.interrogation_20)
        b = int(input(COLOR.BOLD + RU.interrogation_19_1))
        if b == 1:
            print(COLOR.BOLD + RU.story)
    print(COLOR.BOLD + RU.conclusion)


def body():
    start()

    count_places = 0
    places = []
    pharmacy_0 = ''
    while count_places != 4:
        if 1 in places:
            pharmacy_0 = RU.cycle_4
        print(COLOR.BOLD + RU.cycle_0)
        print(COLOR.BOLD + RU.cycle_1)
        print(COLOR.BOLD + RU.cycle_2)
        print(COLOR.BOLD + RU.cycle_3)
        print(COLOR.BOLD + pharmacy_0)
        ans = int(input(RU.cycle_5))
        if ans in places:
            print(COLOR.BOLD + RU.cycle_6)
        else:
            if ans == 1:
                library()
                count_places += 1
                places.append(ans)
            elif ans == 2:
                cinema()
                count_places += 1
                places.append(ans)
            elif ans == 3:
                university()
                count_places += 1
                places.append(ans)
            elif ans == 4:
                pharmacy()
                count_places += 1
                places.append(ans)

    talk()
    call()
    letter()
    evid()


body()
