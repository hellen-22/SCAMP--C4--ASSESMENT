import random

guess = int(input("Guess a number: "))
number = random.randint(0, 20)

if guess < number:
    print("Your guess is too low")
elif guess > number:
    print("Your guess is too high")
else:
    print("Correct! Your guess is right")
    