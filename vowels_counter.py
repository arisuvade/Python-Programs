def main():
    text = get_text()
    result = palindrome_validator(text)
    print(result)


def get_text():
    while True:
        text = input("Text: ")
        if text.isalpha():
            return text
        else:
            continue


def palindrome_validator(text):
    if text == text[::-1]:
        return f"{text.capitalize()} is a palindrome."
    else:
        return f"{text.capitalize()} is not a palindrome."


if __name__ == "__main__":
    main()
