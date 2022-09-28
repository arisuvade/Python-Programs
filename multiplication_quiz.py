import random


def main():
    print("Multiplication Quiz")
    result = gen_quiz()
    print(result)


def gen_quiz():
    score = 0
    numbering = 0

    for _ in range(10):
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        numbering += 1
        answer = x * y

        while True:
            print(f"{numbering}. {x} × {y} = ", end="")
            try:
                user_ans = int(input())
            except ValueError:
                print("That's not a number! Try again")
                continue

            if user_ans == answer:
                print("Correct!")
                score += 1
                break
            else:
                print(f"Wrong! {x} × {y} is {answer}")
                break

    if score <= 4:
        return f"Your score is {score}! Try again!"
    elif score <= 6:
        return f"Your score is {score}! Not bad!"
    else:
        return f"Your score is {score}! Good job!"


if __name__ == "__main__":
    main()
