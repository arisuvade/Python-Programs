def main():
    sum = addition()
    print(f"Sum: {sum:.2f}")


def addition():
    while True:
        try:
            x = float(input("Addend: "))
            y = float(input("Addend: "))
            result = x + y
            break
        except ValueError:
            print("Error: Invalid input")
            continue
    return result


if __name__ == "__main__":
    main()
