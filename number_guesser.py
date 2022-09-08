print("Guess the number 0 - 9")
print("You have 2 chances")
ans = 7
guess_count = 0
guess_limit = 2 # add number to add limit

while guess_count < guess_limit:
    guess = int(input("What number? "))
    guess_count += 1
    if guess == ans:
        print("You're right! Congratulations!")
        break
else:
    print("You're wrong! Try again.")
