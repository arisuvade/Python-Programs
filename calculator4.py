def main():
    operator = get_operator()
    x, y = get_numbers()
    result = solve(x, y, operator)
    print(result)


def get_operator():
    operator = ["plus", "minus", "times", "divide"]
    while True:
        user_input = input("Operator: ").strip().lower()
        try:
            if user_input in operator:
                return user_input
            else:
                raise ValueError
        except ValueError:
            print("Error: Invalid input")
            continue


def get_numbers():
    while True:
        try:
            x = float(input("First: "))
            y = float(input("Second: "))
            return (x, y)
        except ValueError:
            print("Error: Invalid input")
            continue


def solve(x, y, operator):
    if operator == "plus":
        sum = x + y
        return f"Sum: {round(sum, 3)}"
    elif operator == "minus":
        difference = x + y
        return f"Difference: {round(difference, 3)}", x - y
    elif operator == "times":
        product = x + y
        return f"Product: {round(product, 3)}"
    else:
        while True:
            try:
                quotient = x / y
                return f"Qoutient: {round(quotient, 3)}"
            except ZeroDivisionError:
                print("Error: Zero division error")
                x = float(input("First: "))
                y = float(input("Second: "))
                continue


if __name__ == "__main__":
    main()
