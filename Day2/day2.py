"""
# 🎯 Day 02 – Number Guessing Game

This is a fun **Python command-line game** where the player tries to guess a randomly generated number between 1 and 100. The game gives helpful hints after each guess and counts how many attempts the player takes to guess correctly.

---


## ✅ Features

- 🔢 Random number generation (1–100)
- 🔁 Continuous guessing until correct
- 📉 Feedback: "Too low", "Too high", or "Correct"
- 🧠 Tracks number of attempts
- 🚫 Prevents invalid input (optional: add later)

"""

import random
from wsgiref.util import guess_scheme


def random_number():
    print("=== Random Number Guessing Game ===")
    random_number = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != random_number:
        try:
            guess = int(input("Guess: "))
            attempts += 1
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
                continue

            if guess < random_number:
                print("Too low")
            elif guess > random_number:
                print("Too high")
            elif guess == random_number:
                print("Correct")
        except:
            print("Provide valid input")
    print("You took " + str(attempts) + " attempts")
    print("Thank you for playing")




random_number()