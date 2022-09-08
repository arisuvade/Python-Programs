print("Guess the number 0 - 9")
print("You have 2 chances")
ans = 7 # ibahin mo kung gusto mo
guess_count = 0
guess_limit = 2 # dagdagan or bawasan mo yung limit

while guess_count < guess_limit:
    guess = int(input("Anong number? "))
    guess_count += 1
    if guess == ans:
        print("Tama ka! Congrats!")
        break
else:
    print("Mali ka! Ulitin mo.")
