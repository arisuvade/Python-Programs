# Install inflect by pip install inflect or use pip3 in linux

import inflect

p = inflect.engine()


def main():
    num = num_to_words()
    words = p.number_to_words(num)
    print(f"Word: {words.capitalize()}")


def num_to_words():
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
