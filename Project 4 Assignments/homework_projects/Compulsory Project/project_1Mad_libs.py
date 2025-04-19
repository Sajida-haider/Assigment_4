"""
Yahaan ek simple Mad Libs game ka Python code hai. Yeh game user se kuch words leta hai (jaise noun, verb, adjective), aur phir unhein ek story mein use karta hai:
"""
# Mad Libs Game in Python

print("Welcome to the Mad Libs Game!\nPlease enter the following words:")

# Getting user inputs
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
emotion = input("Enter an emotion: ")

# Story using user inputs
story = f"""
One day, I went to the {place} and saw a very {adjective} {animal}.
It {verb} right in front of me! I couldn't believe my eyes.
I picked up a {noun} and ran away while feeling very {emotion}.
It was the most unforgettable day of my life!
"""

# Display the story
print("\nHere's your Mad Libs story:")
print(story)
