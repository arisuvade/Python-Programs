# Install inflect by pip install inflect or use pip3 in linux

import inflect

p = inflect.engine()


def main():
    num = num_to_position()
    position = p.ordinal(num)
    print(f"Position: {position}")


def num_to_position():
    while True:
        try:
            num = int(input("Number: "))
        except ValueError:
            print("Invalid input")
            continue
        else:
            return num


if __name__ == "__main__":
    main()
