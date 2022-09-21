def main():
    word = get_word()
    result = remove_vowels(word)
    print(f"Consonants only: {result}")


def get_word():
    word = input("Word: ")
    return word


def remove_vowels(word):
    vowels = "AEIOUaeiou"
    consonants_only = ""
    for letter in word:
        if letter not in vowels:
            consonants_only += letter
    return consonants_only


if __name__ == "__main__":
    main()
