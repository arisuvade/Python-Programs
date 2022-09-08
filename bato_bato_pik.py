import random

choices = ["BATO", "PAPEL", "GUNTING"]

user = input("Bato, Papel, o Gunting? ").upper()

if user == "BATO":
    computer = random.choice(choices)
    if computer == "BATO":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Tabla!")
    elif computer == "PAPEL":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Talo ka!")
    elif computer == "GUNTING":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Panalo ka!")

if user == "PAPEL":
    computer = random.choice(choices)
    if computer == "BATO":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Talo ka!")
    elif computer == "PAPEL":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Tabla!")
    elif computer == "GUNTING":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Panalo ka!")

if user == "GUNTING":
    computer = random.choice(choices)
    if computer == "BATO":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Panalo ka!")
    elif computer == "PAPEL":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Talo ka!")
    elif computer == "GUNTING":
        print("Ako: " + computer)
        print("Ikaw: " + user)
        print("Tabla!")
else:
    print("Bato, Papel, o Gunting lang wag " + user)
