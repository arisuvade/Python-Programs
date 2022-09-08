import random

die = [1, 2, 3, 4, 5, 6]
user = input("Do you want to roll the dice? (y/n) ")

while True:
    if user == "y":
        roll_again = False
        die_1 = random.choice(die)
        die_2 = random.choice(die)
        print("The dice is rolling...")
        print(str(die_1) + " and " + str(die_2))
        again = input("Do you want to roll the dice again? (y/n) ")
        if again == "y":
            roll_again = True
        elif again == "n":
            print("Ok... bye!")
            break
    elif user == "n":
        print("Ok... bye!")
        break
    else:
        print("To roll the dice, type (y) if yes and (n) if no.")
