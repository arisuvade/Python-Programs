from collections import Counter


def main():
    text, user_list = get_text()
    result = is_anagram(text, user_list)
    print(result)


def get_text():
    length = 1
    user_lists = []
    text = input("Text: ")
    list_length = int(input("List length: "))
    for _ in range(list_length):
        print(f"{length}: ", end="")
        user_list = input()
        user_lists.append(user_list)
        length += 1
    return text, user_lists


def is_anagram(word, list):
    word = word.lower()
    anagrams = []
    for words in list:
        if word != words.lower():
            if Counter(word) == Counter(words.lower()):
                anagrams.append(words)
    return f"Anagrams: {anagrams}"


if __name__ == "__main__":
    main()
