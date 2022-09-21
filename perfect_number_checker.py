def main():
    num = get_number()
    result = is_perfect_number(num)
    print(result)


def get_number():
    while True:
        try:
            num = int(input("Number: "))
            return num
        except ValueError:
            continue


def is_perfect_number(num):
    sum = 0
    for x in range(1, num):
        if num % x == 0:
            sum += x
    perfect_number = sum == num
    if perfect_number:
        return f"{num} is a perfect number"
    else:
        return f"{num} is not a perfect number"


if __name__ == "__main__":
    main()
