"""
User ek number sochta hai, aur computer usay guess karta hai!
"""

print("🤖 Welcome to the Reverse Guess the Number Game!")
print("Think of a number between 1 and 100 and keep it in your mind.")
input("Press Enter when you're ready...")

low = 1
high = 100
attempts = 0

while low <= high:
    guess = (low + high) // 2
    attempts += 1
    print(f"\nIs your number {guess}?")
    response = input("Type (h)igh, (l)ow, or (c)orrect: ").lower()

    if response == "h":
        high = guess - 1
    elif response == "l":
        low = guess + 1
    elif response == "c":
        print(f"\n🎉 Yay! I guessed your number in {attempts} attempts!")
        break
    else:
        print("❌ Please type 'h', 'l', or 'c'.")

if low > high:
    print("\n🤔 Hmm... something doesn't add up! Did you change your number?")
