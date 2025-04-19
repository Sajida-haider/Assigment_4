""""
Yeh task ek simple "Guess My Number" game banane ka hai. Is game mein ek random number hota hai jo computer ke paas hota hai, aur user ko us number ka guess karna hota hai. Program user ko batata hai ke unka guess too high hai ya too low hai, jab tak user sahi number guess nahi kar leta.
Steps:
Computer ek random number choose karega jo 0 se 99 ke beech mein hoga.
User se ek number input liya jayega.
Agar user ka guess too high hai (computer ka number usse chhota hai), toh program batayega "Your guess is too high."
Agar user ka guess too low hai (computer ka number usse bara hai), toh program batayega "Your guess is too low."
Jab user sahi number guess kar leta hai, toh program "Congrats! The number was: [number]" print karega.
"""

import random  # Random number generate karne ke liye

# Random number generate karte hain between 0 and 99
number_to_guess = random.randint(0, 99)

# Loop chalate hain jab tak sahi number guess nahi hota
while True:
    user_guess = int(input("Enter a guess: "))  # User se guess lena

    if user_guess < number_to_guess:
        print("Your guess is too low")  # Agar guess too low hai
    elif user_guess > number_to_guess:
        print("Your guess is too high")  # Agar guess too high hai
    else:
        print(f"Congrats! The number was: {number_to_guess}")  # Agar guess correct hai
        break  # Game khatam ho jata hai jab user sahi guess kar leta hai
4