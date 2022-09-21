def main():
    word = get_word()
    result = reverse(word)
    print(result)


def get_word():
    word = input("Word(s): ")
    return word


def reverse(word):
    words = word.split()
    return (' '.join(words[::-1]))


if __name__ == "__main__":
    main()
