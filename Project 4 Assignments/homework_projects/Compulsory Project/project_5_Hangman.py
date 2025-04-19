import random

def hangman():
    words = ['apple', 'banana', 'grapes', 'orange', 'mango']
    word = random.choice(words)
    guessed = []
    tries = 6

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while tries > 0:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess in word:
            print("Correct!")
        else:
            tries -= 1
            print(f"Wrong! Tries left: {tries}")

        # Show current progress
        display_word = [letter if letter in guessed else '_' for letter in word]
        print(" ".join(display_word))

        # Check win condition
        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", word)
            break
    else:
        print("💀 Game Over! The word was:", word)

hangman()  