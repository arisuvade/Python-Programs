def main():
    product = multiplication()
    print(f"Product: {product:.2f}")


def multiplication():
    while True:
        try:
            x = float(input("Multiplicand: "))
            y = float(input("Multiplier: "))
            result = x * y
            break
        except ValueError:
            print("Error: Invalid input")
            continue
    return result


if __name__ == "__main__":
    main()
