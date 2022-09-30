import random


def main():
    # To play functions
    will_play = to_play()
    result = guessing(will_play)

    # To play again functions
    while will_play:
        if result:
            will_play = to_play(True)
            guessing(will_play)
        else:
            will_play = to_play()
            break


def to_play(play_again=False):
    # To play again
    if play_again is True:

        # Validating input
        print("====================================")
        while True:
            play_again = input("Do you want to play again? [y/n] ").lower()
            if play_again.isalpha():
                if play_again == "y":
                    return True
                elif play_again == "n":
                    return False
                else:
                    print("Invalid input")
                    continue
            else:
                print("Invalid input")
                continue

    # To play
    else:
        # Validating input
        print("====================================")
        while True:
            play = input("Do you want to play? [y/n] ").lower()
            if play.isalpha():
                if play == "y":
                    return True
                elif play == "n":
                    return False
                else:
                    print("Invalid input")
                    continue
            else:
                print("Invalid input")
                continue


def guessing(play):
    # Validating input
    print("------------------------------------")
    while True:
        try:
            level = int(input("Level: [1/2/3] "))
        except ValueError:
            print("Invalid input")
            continue
        else:
            break
    print("------------------------------------")
    print("You only have 5 guesses")

    # Get level
    if level == 1:
        guess_number = random.randint(1, 10)
        print("Guess around 1-10")
    elif level == 2:
        guess_number = random.randint(1, 20)
        print("Guess around 1-20")
    else:
        guess_number = random.randint(1, 30)
        print("Guess around 1-30")

    print("------------------------------------")

    # Guessing
    guess_count = 5
    while play:
        if guess_count >= 1:

            # Validating input
            try:
                user_guess = int(input("Guess: "))
            except ValueError:
                print("Invalid input")
                continue
            else:
                pass

        # Counting mistakes
        while guess_count > 0:
            if user_guess > guess_number:
                guess_count -= 1
                print("Too high!")
                break
            elif user_guess < guess_number:
                guess_count -= 1
                print("Too low!")
                break
            else:
                print("You won! Congrats!")
                return True
        else:
            print("------------------------------------")
            print(f"You loss! It's {guess_number}!")
            return True

    else:
        print("Okay, goodbye!")

        return False


if __name__ == "__main__":
    main()
