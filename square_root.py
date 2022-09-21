import math


def main():
    number = get_number()
    result = square_root(number)
    print(f"Square root: {result:.2f}")


def get_number():
    while True:
        try:
            number = int(input("Number: "))
            return number
        except ValueError:
            continue


def square_root(n):
    return math.sqrt(n)


if __name__ == "__main__":
    main()
