import calendar


def main():
    date = get_date()
    calendar = generate_calendar(date)
    print(f"\n{calendar}")


def get_date():
    while True:
        try:
            month = int(input("Month: "))
            year = int(input("Year: "))
            return (month, year)
        except ValueError:
            print("Invalid input: Numbers only")
            continue


def generate_calendar(date):
    return (calendar.month(date[1], date[0]))


if __name__ == "__main__":
    main()
