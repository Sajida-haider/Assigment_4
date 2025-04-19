"""
Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

Mad Libs is a word game where players are prompted for one word at a time, and the words are eventually filled into the blanks of a word template to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

Here's a sample run (user input is in bold italics):

Please type an adjective and press enter. tiny

Please type a noun and press enter. plant

Please type a verb and press enter. fly

Code in Place is fun. I learned to program and used Python to make my tiny plant fly!


Here's the Python program that prompts the user for an adjective, noun, and verb, and then prints a fun sentence:



Jab program chalega toh pehle yeh bolega:

"Please type an adjective and press enter."

Aap "tiny" type karenge, aur enter press karenge.

Uske baad yeh bolega:

"Please type a noun and press enter."

Aap "plant" type karenge, aur enter press karenge.

Phir yeh bolega:

"Please type a verb and press enter."

Aap "fly" type karenge, aur enter press karenge.

Program aapke inputs ko use kar ke yeh sentence print karega:


Code in Place is fun. I learned to program and used Python to make my tiny plant fly!


"""
# Prompt the user for an adjective, noun, and verb
adjective = input("Please type an adjective and press enter: ")
noun = input("Please type a noun and press enter: ")
verb = input("Please type a verb and press enter: ")

# Create the sentence using the user inputs
sentence = f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!"

# Print the final sentence
print(sentence)
