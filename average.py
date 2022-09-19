import statistics


def main():
    subjects = 0
    grades = []

    while True:
        try:
            input_subjects = int(input("How many subjects? "))
            break
        except ValueError:
            continue

    for _ in range(input_subjects):
        while True:
            print(subjects + 1, ": ", sep="", end="")
            try:
                input_grade = int(input())
                subjects += 1
                grades.append(input_grade)

                break
            except ValueError:
                continue

    average = get_average(grades)
    print(f"Average: {average:.2f}")


def get_average(n):
    return statistics.mean(n)


if __name__ == "__main__":
    main()
