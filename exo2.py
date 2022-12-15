#A CORRIGER

import random

input("Press a button to check your PC status.")
Solution = [Y] or [N]
Status_list = [0, 1, 2, 3]
rand_idx = random.randrange(len(Status_list))
random_status = Status_list[rand_idx]

print("PC status checking result :")

if Status_list [0] == random_status:
    print("Connection error")
    print("Reboot your router.")
    Solution = input("Was the problem solved, [Y], [N] ?")

    if Solution == Y :
        print("PC all clear")
    else:
        print("Problem was sent to helpdesk.")

elif Status_list [1] == random_status:
    print("Temperature error")
    print("Reboot your computer fan.")
    Solution = input("Was the problem solved, [Y], [N] ?")

    if Solution == Y:
        print("PC all clear")
    else:
        print("Problem was sent to helpdesk.")

elif Status_list [2] == random_status:
    print("Driver error")
    print("Driver software update is recquired.")
    Solution = input("Was the problem solved, [Y], [N] ?")

    if Solution == Y:
        print("PC all clear")
    else:
        print("Problem was sent to helpdesk.")

else :
    print("PC all clear")