import time
import random

print("would you like see instructions?")
inst = str(input("If yes then type 'Y' else type 'N'\n>>>"))
if inst == 'Y':
    print("you have to input 1, 2, or 3 numbers. the numbers must be consecutive. whoever reaches the number 21 first looses.")


end = 0

def u_turn():#your turn
    global end
    u = int(input("How many numbers will you enter? \n>>>"))
    for i in range(u):
        if dare[-1] == 21:
            print("You Lose. \nTry Again.")
            end = 1
            break
        else:
            dare.append(dare[-1] + 1)
    if 0 in dare:
        dare.remove(0)
    print(dare)

def c_turn():# computer turn
    global end
    r = random.randint(1,4)
    for i in range(r):
        if dare[-1] == 21:
            print("You Win. \nCongratulations!")
            end = 1
            break
        else:
            dare.append(dare[-1] + 1)
    if 0 in dare:
        dare.remove(0)
    print("Computers turn:\n",dare)






print("Computer is player 2")

dare = [0]
x = input("if you want to go first type 'F' else type 'S' \n>>>")
if x == 'F':
    while end == 0:
        u_turn()
        c_turn()
else:
    while end == 0:
        c_turn()
        u_turn()




time.sleep(5)