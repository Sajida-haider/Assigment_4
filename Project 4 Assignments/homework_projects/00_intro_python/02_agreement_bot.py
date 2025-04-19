
"""
Write a program which asks the user what their favorite animal is, and then always responds with 
"My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

What's your favorite animal? cow

My favorite animal is also cow!
"""
# Yeh program user se uska favorite animal poochta hai 
# aur response deta hai "My favorite animal is also ___!"

# User se input lena
animal = input("What's your favorite animal? ")  

# Response print karna
print(f"My favorite animal is also {animal}")  
