def main():
    num, unit = get_input()
    convertion = height_convert(num, unit)
    print(convertion)


def get_input():
    # use 5.8 not 5'8
    while True:
        try:
            num = float(input("Number: "))
            break
        except ValueError:
            continue
    # cm for centimeters and ft for feet
    while True:
        unit = input("Unit: ").lower()
        if unit == "cm" or unit == "ft":
            return (num, unit)
        else:
            continue


def height_convert(num, unit):
    if unit == "cm":
        convertion = num / 30.48
        str_convertion = str(convertion)
        feet, inch = str_convertion.split(".")
        return f"{feet}'{inch[0]} feet"
    else:
        convertion = num * 30.48
        return f"{convertion:.2f} centimeters"


if __name__ == "__main__":
    main()
