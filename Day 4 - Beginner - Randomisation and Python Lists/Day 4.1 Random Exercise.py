#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

test_speed = int(input("Create a seed number:  "))
random.seed(test_speed)

random_side=random.randint(1,10)

if random_side ==1:
    print("Heads")
else:
    print("Tails")    