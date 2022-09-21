import sys


def main():
    word = get_word()
    consonants_count = consonants_counter(word)
    print(f"Consonants count: {consonants_count}")


def get_word():
    word = input("Word: ")
    words = word.replace(" ", "")
    if words.isalpha():
        return words
    else:
        sys.exit("Error: Invalid input")


def consonants_counter(word):
    vowels = "AEIOUaeiou"
    consonants_count = 0
    for letter in word:
        if letter not in vowels:
            consonants_count += 1
    return consonants_count


if __name__ == "__main__":
    main()
