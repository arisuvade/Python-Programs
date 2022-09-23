from datetime import date
import sys
import inflect


def main():
    # examples of input: 2004-03-01, 2004-3-1, 2022-9-23
    birthdate = input("Date of Birth: ")
    yyyy, mm, dd = get_date(birthdate)
    minutes = get_days(yyyy, mm, dd)
    print(minutes)


def get_date(birthdate):
    try:
        year, month, day = birthdate.split("-")
        if int(year) and int(month) and int(day):
            if len(year) == 4:
                yyyy = int(year)
                mm = int(month)
                dd = int(day)
                return (yyyy, mm, dd)
            else:
                raise ValueError
    except ValueError:
        sys.exit("Invalid date")


def get_days(year, month, day):
    birthdate = date(year, month, day)
    now = date.today()
    difference = now - birthdate
    days = difference.days
    ntw = inflect.engine()
    days_lived = ntw.number_to_words(days)
    return f"{days_lived.capitalize()} days"


if __name__ == "__main__":
    main()
