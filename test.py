#!/usr/bin/python3.9

import os
import time

os.system('clear')
os.system("figlet 'TEST' | lolcat")

test = input("what is 8 x 3?\n>");

if test == "24":
    print("good job");
    pass
elif test == "11":
    print("BOI")
    pass
else:
    print("wrong")
    pass

time.sleep(2)
os.system('clear')
time.sleep(1)
test2 = input("what is 6 + 9\n> ")

if test2 == "15":
    print("Not bad")
    pass
elif test2 == "16":
    print("BOI")
    pass
else:
    print("wrong")
    pass

time.sleep(2)
os.system('clear')
time.sleep(0.2)

os.system("figlet 'LVL 2'|lolcat")
time.sleep(1)

test3 = input("what is 1 x 1 + 1 - 1 - 1 + 1 x 1\n> ")
answer1 = (1 * 1 + 1 - 1 - 1 + 1 * 1)

if test3 == "1":
    print("impressive")
    pass
elif test3 == "2":
    print("BOI")
    pass
else:
    print("NOPE the answer vvv")
    print(int(answer1))
    pass

time.sleep(2)

test4 = input("\nwhat is 50 + 50 - 100 + 30 - 20 + 100 - 50 - 30 + 10 + 40 / 2 ???\n> ")
answer2 = (50 + 50 - 100 + 30 - 20 + 100 - 50 - 30 + 10 + 40 / 2)

if test4 == "60" :
    print("lol")
    pass
elif test4 == "80":
    print ("IKR but no")
else:
    print ("EEEEEEEEE")
    print(int(answer2))
    pass

time.sleep(2)
os.system('clear')
os.system("figlet 'TEST'|lolcat")
time.sleep(30)
