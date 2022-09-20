def main():
    quotient = division()
    print(f"Quotient: {quotient:.2f}")


def division():
    while True:
        try:
            x = float(input("Dividend: "))
            y = float(input("Divisor: "))
            result = x / y
            break
        except (ValueError, ZeroDivisionError):
            print("Error: Invalid input")
            continue
    return result


if __name__ == "__main__":
    main()
