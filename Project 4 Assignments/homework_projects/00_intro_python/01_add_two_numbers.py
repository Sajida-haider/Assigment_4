

"""
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

    Prompt the user to enter the first number.

    Read the input and convert it to an integer.

    Prompt the user to enter the second number.

    Read the input and convert it to an integer.

    Calculate the sum of the two numbers.

    Print the total sum with an appropriate message.

The provided solution demonstrates a working implementation of this problem, where the main() function guides the user through the process of entering two numbers and displays their sum.




Code Samjhne se Pehle Concept Samjho:
📌 Humein do numbers input lene hain, unka sum calculate karna hai, aur result print karna hai."""

def sum():  
    num1 = int(input("Enter the first number: "))  # Pehla number input lo
    num2 = int(input("Enter the second number: "))  # Dusra number input lo

    total = num1 + num2  # Dono numbers ka sum calculate karo

    print("The total sum is:", total)  # Result print karo

# Function call karna zaroori hai
sum()
