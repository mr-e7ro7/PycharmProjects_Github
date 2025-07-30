import time
import random


print("WELCOME TO THE NUMBER GUESSING GAME")
print("-----------------------------------")
start = int(input("select starting point of range:"))
end = int(input("select end point of range:"))

n = random.randint(start, end+1)
c = 1
while 1:
    print("Guess ", c, ":", sep = "", end = "")
    g = int(input())
    if g == n:
        print("congratulations, you got it!")
        c += 1
        print("Total Guesses:", c)
        break
    elif g < n:
        print("Too low")
        c += 1
    else:
        print("Too high")
        c += 1

print("Thank you for playing")




time.sleep(5)