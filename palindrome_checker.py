import sys


def main():
    text = get_text()
    result = palindrome_validator(text)
    print(result)


def get_text():
    text = input("Text: ")
    if text.isalpha():
        return text
    else:
        sys.exit("Invalid input")


def palindrome_validator(text):
    if text == text[::-1]:
        return f"{text.capitalize()} is a palindrome."
    else:
        return f"{text.capitalize()} is not a palindrome."


if __name__ == "__main__":
    main()
