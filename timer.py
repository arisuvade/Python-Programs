import time


def main():
    count = get_time()
    countdown(count)


def get_time():
    while True:
        try:
            count = int(input("Seconds: "))
            return count
        except ValueError:
            continue


def countdown(cd):
    while cd:
        minutes, seconds = divmod(cd, 60)
        timer = "{:02d}:{:02d}".format(minutes, seconds)
        print(f"Timer: {timer}", end="\r")
        time.sleep(1)
        cd -= 1
    print("Timer ended!")


if __name__ == "__main__":
    main()
