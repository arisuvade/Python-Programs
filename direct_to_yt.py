# Download pywhatkit using pip(pip3 in linux) install
# pywhatkit in your terminal

import pywhatkit
import requests


def main():
    url = get_url()
    pywhatkit.playonyt(url)


"""Valid input"""
# https://www.youtube.com/watch?v=dQw4w9WgXcQ
# https://youtube.com/watch?v=dQw4w9WgXcQ

"""Invalid inputs"""
# www.youtube.com/watch?v=dQw4w9WgXcQ
# youtube.com/watch?v=dQw4w9WgXcQ
# watch?v=dQw4w9WgXcQ
# dQw4w9WgXcQ


def get_url():
    while True:
        url = input("YouTube URL: ").strip()

        try:
            request = requests.get(url)
        except requests.RequestException:
            print("Invalid YouTube URL")
            continue

        # Checking if URL exist
        if "Video unavailable" in request.text:
            print("YouTube URL doesn't exist")
        else:
            print("Dirrecting to YouTube...")
            return url


if __name__ == "__main__":
    main()
