import math
import sys


def main():
    number = get_number()
    result = square_root(number)
    print(f"Square root: {result:.2f}")


def get_number():
    try:
        number = int(input("Number: "))
    except ValueError:
        sys.exit("Error: Invalid input")
    return number


def square_root(n):
    return math.sqrt(n)


if __name__ == "__main__":
    main()
