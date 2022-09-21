def main():
    num = get_number()
    result = is_prime(num)
    print(result)


def get_number():
    while True:
        try:
            num = int(input("Number: "))
            return num
        except ValueError:
            continue


def is_prime(num):
    divisible = 0
    for i in range(1, num + 1):
        if num % i == 0:
            divisible += 1
    if divisible == 2:
        return f"{num} is a prime number."
    return f"{num} is not a prime number."


if __name__ == "__main__":
    main()
