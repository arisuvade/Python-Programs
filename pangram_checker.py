def main():
    text = get_text()
    result = is_pangram(text)
    print(result)


def get_text():
    text = input("Text: ")
    return text


def is_pangram(text):
    alphabet = list(map(chr, range(97, 123)))
    formattedString = ''.join(c for c in text if c.isalpha()).lower()
    result = set(alphabet) == set(formattedString)
    if result:
        return f"{text} is a pangram"
    else:
        return f"{text} is not a pangram"


if __name__ == "__main__":
    main()
