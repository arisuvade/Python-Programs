import random


def main():
    user, com = get_choice()
    result = rps(user, com)
    print(f"Com: {com}")
    print(f"Result: {result}")


def get_choice():
    choices = ["Rock", "Paper", "Scissor"]
    com = random.choice(choices)
    while True:
        user = input("User: ").strip().capitalize()
        if user in choices:
            return (user, com)


def rps(user, com):
    choices = {"Rock": 0, "Paper": 1, "Scissor": 2}
    results = ["Draw!", "You won!", "You loss!"]
    result = choices[user] - choices[com]
    return results[result]


if __name__ == "__main__":
    main()
