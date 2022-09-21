import random
import sys


def main():
    length = password_length()
    password = password_generator(length)
    print(f"Password: {password}")


def password_length():
    try:
        length = int(input("Length: "))
    except ValueError:
        sys.exit("Error: Invalid input")
    return length


def password_generator(length):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*"
    characters = lower_case + upper_case + numbers + symbols
    password = "".join(random.sample(characters, length))
    return password


if __name__ == "__main__":
    main()
