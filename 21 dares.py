import time
import random

print("would you like see instructions?")
inst = str(input("If yes then type 'Y' else type 'N'\n>>>"))
if inst == 'Y':
    print("you have to input 1, 2, or 3 numbers. the numbers must be consecutive. whoever reaches the number 21 first looses.")


print("Computer is player 2")

dare = []
x = input("if you want to go first type 'F' else type 'S' \n>>>")
if x == 'F':
    u = int(input("How many numbers will you enter? \n>>>"))
    for i in range(u):
        a = int(input(">>>"))
        dare.append(a)
    print(dare)


time.sleep(5)