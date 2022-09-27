def main():
    num, unit = get_input()
    convertion = temp_convert(num, unit)
    print(convertion)


def get_input():
    while True:
        try:
            num = int(input("Number: "))
            break
        except ValueError:
            continue
    # f for fahrenheit and c for celcius
    while True:
        unit = input("Unit: ").lower()
        if unit == "f" or unit == "c":
            return (num, unit)
        else:
            continue


def temp_convert(num, unit):
    if unit == "f":
        convertion = (num - 32) * .5556
        return f"{convertion:.2f} celcius"
    else:
        convertion = num * 1.8 + 32
        return f"{convertion:.2f} fahrenheit"


if __name__ == "__main__":
    main()
