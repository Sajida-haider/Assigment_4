"""
 Yahaan ek simple aur fun "Guess the Number" game ka Python project hai jahan computer ek number sochta hai, aur user usay guess karta hai. 💡
 """
 # Guess the Number Game - Project 2

import random

print("🎯 Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100...")

# Step 1: Computer thinks of a random number
secret_number = random.randint(1, 100)
attempts = 0

# Step 2: User keeps guessing until they are correct
while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempts} tries!")
            break

    except ValueError:
        print("Please enter a valid number.")


