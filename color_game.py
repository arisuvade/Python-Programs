import random
import sys

MIN_DEPOSIT = 5
MIN_BET = 5
COLORS = ["Yellow", "White", "Pink", "Blue", "Red", "Green"]


def get_deposit():
    while True:
        try:
            deposit = int(input("Deposit: ₱"))
            if MIN_DEPOSIT >= deposit % MIN_BET == 0 and deposit != 0:
                return deposit
            print("Invalid deposit")
        except ValueError:
            print("Invalid input")


def get_bet():
    while True:
        try:
            bet = int(input("Bet: ₱"))
            if MIN_BET >= bet % MIN_BET == 0 and bet != 0:
                return bet
            print("Invalid bet")
        except ValueError:
            print("Invalid input")


def colors_count():
    while True:
        try:
            count = int(input("Colors count[1-6]: "))
        except ValueError:
            print("Invalid input")
            continue

        if count in range(1, 7):
            return count
        print("Invalid number")


def get_color():
    while True:
        color = input("Color: ").capitalize()
        if color in COLORS:
            return color
        print("Invalid color")


def roll():
    return random.choice(COLORS)


def color_game(colors, bet, deposit):
    balance = deposit

    d1, d2, d3 = dice = [roll(), roll(), roll()]
    print("Winning colors:", *dice)

    for color in colors:
        if color not in dice:
            balance -= bet

    for color in colors:
        if color == d1:
            balance += bet
        if color == d2:
            balance += bet
        if color == d3:
            balance += bet

    return balance


def main():
    deposit = get_deposit()
    play = True
    while play:
        bet = get_bet()
        while True:
            if deposit < bet:
                print("Not enough balance")
                bet = get_bet()
                continue
            break

        while True:
            how_many = colors_count()
            total_bet = bet * how_many
            if deposit < total_bet:
                print("Not enough balance")
                bet = get_bet()
                continue
            break

        print(f"Total bet: ₱{total_bet}")
        print("Colors: Yellow, White, Pink, Red, Blue, and Green")
        colors = []
        for _ in range(how_many):
            colors.append(get_color())

        balance = color_game(colors, bet, deposit)
        print(f"Balance: ₱{balance}")
        deposit = balance
        if deposit == 0:
            print("You have no balance to play again")
            sys.exit()

        while True:
            play_again = input("Play again [y/n]: ")
            if play_again == "y":
                play = True
                break
            elif play_again == "n":
                play = False
                break
            else:
                print("Invalid input")

    print(f"You left with ₱{deposit}")


if __name__ == "__main__":
    main()
