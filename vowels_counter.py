import sys


def main():
    word = get_word()
    vowels_count = vowels_counter(word)
    print(f"Vowels count: {vowels_count}")


def get_word():
    word = input("Word: ")
    words = word.replace(" ", "")
    if words.isalpha():
        return words
    else:
        sys.exit("Error: Invalid input")


def vowels_counter(word):
    vowels = "AEIOUaeiou"
    vowels_count = 0
    for letter in word:
        if letter in vowels:
            vowels_count += 1
    return vowels_count


if __name__ == "__main__":
    main()
