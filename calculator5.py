class Math:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        try:
            quotient = x / y
            return quotient
        except ZeroDivisionError:
            return "Infinity"


def main():
    operator = get_operator()
    x, y = get_number(operator)
    result = operation(operator, x, y)

    match operator:
        case "add":
            print(f"Sum: {result}")
        case "subtract":
            print(f"Difference: {result}")
        case "multiply":
            print(f"Product: {result}")
        case "divide":
            print(f"Quotient: {result}")


def get_operator():
    while True:
        operator = input("Operator: ").lower().strip()
        if operator in ["add", "subtract", "multiply", "divide"]:
            return operator
        else:
            print("Invalid input")


def get_number(operator):
    while True:
        match operator:
            case "add":
                try:
                    x = float(input("Addend: "))
                    y = float(input("Addend: "))
                    break
                except ValueError:
                    print("Invalid input")
            case "subtract":
                try:
                    x = float(input("Minuend: "))
                    y = float(input("Subtrahend: "))
                    break
                except ValueError:
                    print("Invalid input")
            case "multiply":
                try:
                    x = float(input("Multiplicand: "))
                    y = float(input("Multiplier: "))
                    break
                except ValueError:
                    print("Invalid input")
            case "divide":
                try:
                    x = float(input("Dividend: "))
                    y = float(input("Divisor: "))
                    break
                except ValueError:
                    print("Invalid input")

    return (x, y)


def operation(operator, x, y):
    match operator:
        case "add":
            result = Math.add(x, y)
        case "minus":
            result = Math.subtract(x, y)
        case "multiply":
            result = Math.multiply(x, y)
        case "divide":
            result = Math.divide(x, y)

    # To check if it is a whole number
    if result % 1 == 0:
        return int(result)
    else:
        return result


if __name__ == "__main__":
    main()
