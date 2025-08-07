import time
import random

print("would you like see instructions?")
inst = str(input("If yes then type 'Y' else type 'N'\n>>>"))
if inst == 'Y' or inst == 'y':
    print("you have to input 1, 2, or 3 numbers. the numbers must be consecutive. whoever reaches the number 21 first looses.")


def u_turn():#your turn
    global dare
    global end
    u = int(input("How many numbers will you enter? \n>>>"))

    if len(dare) + u < 21:
        for i in range(u):
            dare.append(dare[-1] + 1)
    else:
        print("You Lose. \nTry Again.", sep = "")
        end = 1

    if 0 in dare:
        dare.remove(0)

    if end != 1:
        print(dare)

def c_turn():# computer turn
    global dare
    global end
    r = random.randint(1,3)

    if len(dare) + r < 21:
        for i in range(r):
            dare.append(dare[-1] + 1)
    else:
        print("You Win. \nCongratulations!")
        end = 1

    if 0 in dare:
        dare.remove(0)
    if end != 1:
        print("Computers turn:\n",dare)






print("Computer is player 2")

dare = [0]
end = 0
x = input("if you want to go first type 'F' else type 'S' \n>>>")
if x == 'F':
    while 1:
        u_turn()
        if end==1:
            break

        c_turn()
        if end==1:
            break
else:
    while 1:
        c_turn()
        if end==1:
            break

        u_turn()
        if end==1:
            break




#time.sleep(5)