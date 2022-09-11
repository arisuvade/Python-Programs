print("Calculator")
print("""
Addition(A)
Subtraction(S)
Multiplication(M)
Division(D)
""")

op = input("What operation? ").lower()

numbers = {
    "n1": float(input("First Number: ")),
    "n2": float(input("Second Number: "))
}

first = numbers.get("n1")
second = numbers.get("n2")


def math(fn, sn):
    if op == "a":
        ans = fn + sn
        print(f"Answer: {ans}")
    elif op == "s":
        ans = fn - sn
        print(f"Answer: {ans}")
    elif op == "m":
        ans = fn * sn
        print(f"Answer: {ans}")
    elif op == "d":
        ans = fn / sn
        print(f"Answer: {ans}")


math(first, second)
