"""
Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

Ye program do dice ko teen dafa roll karne ka simulation hai. Har dafa do dice ka result print hoga. Is program ka maqsad variable scope (matlab variable kis jagah accessible hota hai) samjhna hai.

"""
import random

def roll_dice():
    die1 = random.randint(1, 6)  # Pehla dice ka random number
    die2 = random.randint(1, 6)  # Dosra dice ka random number
    print(f"Die 1: {die1}, Die 2: {die2}")  # Result print karna

# Teen dafa dice roll karna
for _ in range(3):
    roll_dice()


