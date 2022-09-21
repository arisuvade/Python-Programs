def main():
    sides = get_side()
    area = get_area(sides)
    print(f"Area: {area}")


def get_side():
    while True:
        try:
            a = int(input("a: "))
            b = int(input("b: "))
            c = int(input("c: "))
            return (a, b, c)
        except ValueError:
            print("Error: Invalid input")
            continue


def get_area(sides):
    s = (sides[0] + sides[1] + sides[2]) / 2
    area = (s*(s-sides[0])*(s-sides[1])*(s-sides[2])) ** 0.5
    return area


if __name__ == "__main__":
    main()
