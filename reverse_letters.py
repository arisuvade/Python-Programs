def main():
    text = input("Text: ")
    result = reverse(text)
    print(f"Reversed: {result}")


def reverse(text):
    r_text = ""
    for character in text:
        r_text = character + r_text
    return r_text


if __name__ == "__main__":
    main()
