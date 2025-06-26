from random import randint 
from random import choice
d = int(input(("What size dize are you rolling? ")))
print(f"You have selected a d{d}")
while True:
    roll_accept= input("Do you want to roll your dice? Y/N ")
    accept_list = ["y", "Y", "YES"]
    reject_list = ["n", "N", "NO"]
    if roll_accept in accept_list:
        roll = (randint(1, d))
        print(f"You rolled a {roll}")   
    elif roll_accept in reject_list:
        continue
