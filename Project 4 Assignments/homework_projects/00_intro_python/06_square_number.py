"""
Ask the user for a number and print its square (the product of the number times itself).

Here's a sample run of the program (user input is in bold italics):

Type a number to see its square: 4

4.0 squared is 16.0

Yeh program user se ek number input lega aur uska square calculate karke print karega:

"""
# User se number input lena aur float mein convert karna
num = float(input("Type a number to see its square: "))

# Square calculate karna
square = num * num  

# Result print karna
print(f"{num} squared is {square}")  
