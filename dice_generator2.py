import random


def main():
    die1, die2 = dice()
    print(die1, die2)


def dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return (die1, die2)


if __name__ == "__main__":
    main()
