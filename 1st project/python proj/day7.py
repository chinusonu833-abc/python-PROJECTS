import time
import random

chars = "ggjh vjvgfbhuhuib"

password = input("Set password: ")

print("\nAccessing database.....\n")

guess = ""

while guess != password:
    guess = ""

    for i in range(len(password)):
        guess += random.choice(chars)

    print("Trying......!", guess)
    time.sleep(0.01)

print("\nPassword cracked:", password)