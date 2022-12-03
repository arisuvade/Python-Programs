from random import randint

print("Guess the Number from 0 to 9!")

target = randint(0, 9)
limit = 5

while limit > 0:
    try:
        guess = int(input("Guess: "))
        if guess not in range(0, 10):
            print("Guess 0 to 9 only.")
            continue
    except ValueError:
        print("Invalid input")
        continue

    if guess == target:
        print(f"Correct! It's {target}")
        break

    limit -= 1
    if limit != 0:
        print("Too high!" if guess > target else "Too low!")
        print(f"{limit} guess remaining.")

else:
    print(f"Wrong! It's {target}.")
