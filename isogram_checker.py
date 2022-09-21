def main():
    text = get_text()
    result = is_isogram(text)
    print(result)


def get_text():
    while True:
        text = input("Text: ")
        if text.isalpha():
            return text
        else:
            continue


def is_isogram(text):
    word = text.lower()
    letter_list = []
    for letter in word:
        if letter.isalpha():
            if letter in letter_list:
                return f"{text.capitalize()} is not an isogram"
            letter_list.append(letter)
    return f"{text.capitalize()} is an isogram"


if __name__ == "__main__":
    main()
