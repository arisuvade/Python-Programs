import random


def main():
    print(
        """===================
Rock Paper Scissor
-------------------"""
    )
    user_choice = get_userchoice()
    com_choice = get_comchoice()
    print(f"User: {user_choice}")
    print(f"Comp: {com_choice}")
    print("-------------------")
    result = battle(user_choice, com_choice)
    print(result)
    print("===================")


def get_userchoice():
    choices = ["Rock", "Paper", "Scissor"]
    while True:
        choice = input("Choice: ").capitalize()
        print("-------------------")
        if choice in choices:
            return choice
        else:
            print("Invalid input")
            print("-------------------")
            continue


def get_comchoice():
    choices = ["Rock", "Paper", "Scissor"]
    choice = random.choice(choices)
    return choice


def battle(user, com):
    if user == "Rock":
        match com:
            case "Rock":
                return "Draw!"
            case "Paper":
                return "You loss!"
            case "Scissor":
                return "You won!"
    elif user == "Paper":
        match com:
            case "Rock":
                return "You won!"
            case "Paper":
                return "Draw!"
            case "Scissor":
                return "You loss!"
    else:
        match com:
            case "Rock":
                return "You loss!"
            case "Paper":
                return "You won!"
            case "Scissor":
                return "Draw!"


if __name__ == "__main__":
    main()
