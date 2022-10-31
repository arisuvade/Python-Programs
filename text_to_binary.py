while True:
    text = input("Text: ")
    print("Binary: ", end="")
    try:
        for i in text:
            print(format(ord(i), "b"), end=" ")
    except ValueError:
        print("Invalid binary")
        continue
    else:
        print()
        break
