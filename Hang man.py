import time
import random






words = ['rainbow', 'computer', 'science', 'programming','python', 'mathematics', 'player', 'condition','reverse', 'water', 'board', 'geeks']

w = random.choice(words)
w1 = list(w)
l = len(w)
g = 6
x = "_" * l

print("you have a total of  6 guesses.\n\n_______________________________")
print("your word has", l, "letters")
while g > 0:
    print("you have", g, "guesses")
    print(x)
    c = input("Take a guess: ")

    if len(c) == 1:
        if c in w:
            print("good job")
            temp = x
            x = ""
            t1 = list(temp)
            for i in range(len(w)):

                if t1[i] != "_":
                    x += t1[i]
                elif t1[i] == "_" and c == w1[i]:
                    x += c

                else:
                    x += "_"


        else:
             print("Sorry, try again")
             g -= 1

    elif c == w:
        print("congratulations")
        break
    else:
        print("Sorry, try again")
        g -= 1


time.sleep(5)
