import random

answer = random.randint(1,11)

guess = int(input("Guess:"))

while guess != answer:
    if guess < answer:
        print("Too low")
    else:
        print("Too high")
    guess = int(input("Guess:"))