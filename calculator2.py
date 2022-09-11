print("Calculator")
print("------------")

first = float(input("First Number: "))
symbol = input("Symbol: (+, -, *, /) ")
second = float(input("Second Number: "))


def add():
    answer = first + second
    print(str(answer))


def minus():
    answer = first - second
    print(str(answer))


def multiply():
    answer = first * second
    print(str(answer))


def divide():
    answer = first / second
    print(str(answer))


if symbol == "+":
    add()
if symbol == "-":
    minus()
if symbol == "*":
    multiply()
if symbol == "/":
    divide()
