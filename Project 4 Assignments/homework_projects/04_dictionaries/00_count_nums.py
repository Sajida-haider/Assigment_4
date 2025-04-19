"""
Yeh program 10 random numbers ko print karne ke liye Python ki random.randint() function ka use karta hai. Yeh function har bar ek random integer generate karta hai jo diye gaye range (1 se 100) ke beech hota hai.
"""
import random

N_NUMBERS = 10  # Kitne random numbers generate karne hain
MIN_VALUE = 1    # Minimum value jo random number ho sakta hai
MAX_VALUE = 100  # Maximum value jo random number ho sakta hai

def main():
    # Loop chalana jo 10 random numbers print karega
    for _ in range(N_NUMBERS):
        print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")

if __name__ == '__main__':
    main()
