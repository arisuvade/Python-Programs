def main():
    difference = subtraction()
    print(f"Difference: {difference:.2f}")


def subtraction():
    while True:
        try:
            x = float(input("Minuend: "))
            y = float(input("Subtrahend: "))
            result = x - y
            break
        except ValueError:
            print("Error: Invalid input")
            continue
    return result


if __name__ == "__main__":
    main()
