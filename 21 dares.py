import time
import random

print("would you like see instructions?")
inst = str(input("If yes then type 'Y' else type 'N'\n>>>"))
if inst == 'Y':
    print("you have to input 1, 2, or 3 numbers. the numbers must be consecutive. whoever reaches the number 21 first looses.")

def U_Turn():#your turn
    u = int(input("How many numbers will you enter? \n>>>"))
    for i in range(u):
        if dare[-1] == 21:
            print("You Lose. \nTry Again.")
            break
        else:
            dare.append(dare[-1] + 1)
    if 0 in dare:
        dare.remove(0)
    print(dare)

def C_Turn():# computer turn
    r = random.randint(1,4)
    for i in range(r):
        if dare[-1] == 21:
            print("You Win. \nCongratulations!")
            break
        else:
            dare.append(dare[-1] + 1)
    if 0 in dare:
        dare.remove(0)
    print(dare)






print("Computer is player 2")

dare = []
x = input("if you want to go first type 'F' else type 'S' \n>>>")
if x == 'F':





time.sleep(5)