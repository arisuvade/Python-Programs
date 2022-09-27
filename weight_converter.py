def main():
    num, unit = get_input()
    convertion = weight_convert(num, unit)
    print(convertion)


def get_input():
    while True:
        try:
            num = float(input("Number: "))
            break
        except ValueError:
            continue
    # kg for kilograms and lbs for pounds
    while True:
        unit = input("Unit: ").lower()
        if unit == "kg" or unit == "lbs":
            return (num, unit)
        else:
            continue


def weight_convert(num, unit):
    if unit == "kg":
        convertion = num * 2.20462
        return f"{convertion:.2f} pounds"
    else:
        convertion = num / 2.20462
        return f"{convertion:.2f} kilos"


if __name__ == "__main__":
    main()
