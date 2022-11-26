from string import ascii_letters, digits, punctuation
import random

text = ascii_letters + digits + punctuation
length = 8
passw = "".join(random.choice(text) for _ in range(length))
print(f"Password: {passw}")
