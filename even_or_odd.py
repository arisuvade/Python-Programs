def main():
    num = get_number()
    result = even_or_odd(num)
    print(result)


def get_number():
    while True:
        try:
            num = int(input("Number: "))
            return num
        except ValueError:
            continue


def even_or_odd(num):
    if num % 2 == 0:
        return f"{num} is an even number."
    else:
        return f"{num} is an odd number."


if __name__ == "__main__":
    main()
