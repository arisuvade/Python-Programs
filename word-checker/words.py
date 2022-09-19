words = []

word = input("Word: ").lower()

with open("words.txt") as file:
    for line in file:
        words.append(line.rstrip())

if word in words:
    print(f"{word.capitalize()} is on the dictionary.")
else:
    print(f"{word.capitalize()} is not on the dictionary.")
