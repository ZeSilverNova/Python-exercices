#A CORRIGER

import random

Numbers = [0 , 1 , 2 , 3 , 4 , ... , 997 , 998 , 999 , 1000 ]

rand_idx = random.randrange(len(Numbers))
Password = Numbers[rand_idx]
Guess = int(input("Password is a number between 0 and 1000, try to guess it."))

while Guess != Password:
    Guess = input("Password is a number between 0 and 1000, try to guess it.")

    if Guess == Password :
        print("Open sesame ! The password was" + Password)
    elif int(Guess) < Password :
        print("Sorry, this wasn't the password. Try something higher.")
    else:
        print("Sorry, this wasn't the password. Try something lower.")


