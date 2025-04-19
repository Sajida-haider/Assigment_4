
"""
Yeh task tumhein ek simple Joke Bot likhna hai. Bot user se pehle "What do you want?" poochta hai. Agar user "Joke" input karta hai, toh bot ek joke print karega. Agar user kuch aur type karega, toh bot kehta hai "Sorry I only tell jokes."

Task me diye gaye constants:

PROMPT: User ko prompt dene wala message ("What do you want?")

JOKE: Joke jo print karni hai jab user "Joke" enter kare

SORRY: Message jo print hoga jab user kuch aur input kare
"""


PROMPT = "What do you want? "
JOKE = "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY = "Sorry I only tell jokes"

def main():
    user_input = input(PROMPT)
    user_input = user_input.strip().lower()

    if user_input == "joke":
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
