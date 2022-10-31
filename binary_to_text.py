while True:
    binary = input("Binary: ")
    print("Text: ", end="")
    try:
        for i in binary.split(" "):
            print(chr(int(i, 2)), end="")
    except ValueError:
        print("Invalid binary")
        continue
    else:
        print()
        break
