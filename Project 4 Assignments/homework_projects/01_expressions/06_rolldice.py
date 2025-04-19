"""
Simulate rolling two dice, and prints results of each roll as well as the total.

Ye program do dice roll karne ka simulation karta hai aur unke results aur total ko print karta hai.
Chalo isko step-by-step samajhte hain! 😊

"""
import random  # Random library ko import karna jo dice roll karne mein madad karega

# Number of sides on each die to roll (yeh variable dice ke sides ko define karta hai)
NUM_SIDES: int = 6

def main():
    # Dice ko roll karte hain
    die1: int = random.randint(1, NUM_SIDES)  # First die ka random number (1 se 6)
    die2: int = random.randint(1, NUM_SIDES)  # Second die ka random number (1 se 6)
    
    # Dono dice ka total nikalte hain
    total: int = die1 + die2
    
    # Results print karte hain
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Ye line isliye zaroori hai taake program properly run ho                          
if __name__ == '__main__':
    main()"""
