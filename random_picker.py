import random


def main():
    length = get_length()
    picked = get_list(length)
    print(f"Picked: {picked}")


def get_length():
    while True:
        try:
            lenght = int(input("Length list: "))
            return lenght
        except ValueError:
            continue


def get_list(length):
    list_number = 1
    list = []
    for _ in range(length):
        print(f"{list_number}: ", end="")
        user_list = input()
        list.append(user_list)
        list_number += 1
    random_list = random.choice(list)
    return random_list


if __name__ == "__main__":
    main()
