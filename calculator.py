print("Calculator")
print("\n")

first_number = float(input("First Number: ")) # change mo sa int if gusto mo whole number
symbol = input("Arithmetic symbol(+, -, *, /): ")
second_number = float(input("Second Number: "))

if symbol == "+":
    answer = first_number + second_number
    print("Answer: " + str(answer))
elif symbol == "-":
    answer = first_number - second_number
    print("Answer: " + str(answer))
elif symbol == "*":
    answer = first_number * second_number
    print("Answer: " + str(answer))
elif symbol == "/":
    answer = first_number / second_number
    print("Answer: " + str(answer))
