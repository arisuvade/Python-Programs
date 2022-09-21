def main():
    word = get_word()
    result = remove_consonants(word)
    print(f"Vowels only: {result}")


def get_word():
    word = input("Word: ")
    return word


def remove_consonants(word):
    vowels = "AEIOUaeiou "
    vowels_only = ""
    for letter in word:
        if letter in vowels:
            vowels_only += letter
    return vowels_only


if __name__ == "__main__":
    main()
