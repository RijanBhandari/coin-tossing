import random
from time import sleep
from os import system, name
from threading import Thread
from sound import sound


def cls():
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def forexit():
    print("BYE", end="", flush=True) # flush= true is ued to clear the output buffer defult is false
    aa = 0
    while 1:
        sleep(0.71)
        print('.', end="", flush=True)
        aa = aa + 1
        if aa == 2:
            break
def tossing():
    print("tossing", end='', flush=True)
    aa = 0
    while 1:
        print('.', end="", flush=True)
        aa = aa + 1
        sleep(1)
        if aa == 4:
            cls()
            break


def process():
    while 1:
        sec = ['heads', 'tails'] # a list
        choice = random.choice(sec) # random.choice() selects a term from list
        t1 = Thread(target=sound) # thread(target = ) from thereading is used to run two function at same time 
        t1.start()
        t2 = Thread(target=tossing())
        t2.start()
        if choice == sec[0]:
            cls()
            print("\nHEADS")
        else:
            cls()
            print("\nTAILS")
        sleep(1.5)
        b = (input("\n\n\nPress Enter to toss again and N to exit: "))
        b = b.upper() # variable.upper() to print uppercase string
        if b == 'N':
            forexit()
            break
        elif b == '':
            cls()
            continue
        else:
            print("Invalid input :(\nTossing again")
            sleep(2) # sleep from time.sleep(parameter) is used to stop the program for given seconds


input('Press enter to toss: ')
process()
