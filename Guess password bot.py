#AMELIORABLE

import random
list1 = []

for i in range(1000):
    #for i in range (1000) = tant qu'on a pas atteint range 1000 on continue (ce qui fait la liste)
    list1.append(i)
    #append va rajouter des éléments à une liste

rand_idx = random.randrange(len(list1))
random_num = list1[rand_idx]

print("Random selected number is : " + str(random_num))
