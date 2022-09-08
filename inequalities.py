print("Greater than, Less than, or Equal")

first = int(input("First Number: "))  # change mo sa float if gusto mo ng may decimals
second = int(input("Second Number: "))

if first > second:
    print(str(first) + " is greater than (>) " + str(second))
elif first < second:
    print(str(first) + " is less than (<) " + str(second))
else:
    print(str(first) + " is equals (=) to " + str(second))
