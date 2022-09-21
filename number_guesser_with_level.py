import random


def main():
    level = get_level()
    guess = generate_guess(level)
    result = guess_counter(guess)
    print(result)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 3 or level <= 0:
                continue
            break
        except ValueError:
            continue
    if level == 1:
        return 1
    elif level == 2:
        return 2
    else:
        return 3


def generate_guess(level):
    if level == 1:
        guess_number = random.randint(0, 9)
    elif level == 2:
        guess_number = random.randint(0, 19)
    else:
        guess_number = random.randint(0, 29)
    return guess_number


def guess_counter(guess):
    guess_count = 0
    while True:
        if guess_count != 5:
            try:
                user_answer = int(input("Guess: "))
                guess_count += 1
                pass
            except ValueError:
                continue
            if user_answer < guess:
                print("Too low!")
                continue
            elif user_answer > guess:
                print("Too high!")
                continue
            else:
                return "Right!"
        else:
            return f"Number: {guess}"


if __name__ == "__main__":
    main()
