def main():
    text = get_text()
    result = is_palindrome(text)
    print(result)


def get_text():
    text = input("Text: ")
    return text


def is_palindrome(text):
    if text == text[::-1]:
        return f"{text.capitalize()} is a palindrome."
    else:
        return f"{text.capitalize()} is not a palindrome."


if __name__ == "__main__":
    main()
