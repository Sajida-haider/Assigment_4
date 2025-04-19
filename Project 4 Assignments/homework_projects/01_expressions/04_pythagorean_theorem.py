"""
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, is a fundamental relation in geometry. It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

BC ** 2 = AB ** 2 + AC ** 2

Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

Here's a sample run of the program (user input is in bold italics):

Enter the length of AB: 3

Enter the length of AC: 4

The length of BC (the hypotenuse) is: 5.0


How This Works:
User se input lena: float(input(...)) ke zariye dono sides input lete hain.

Formula lagana: math.sqrt(AB**2 + AC**2) ka use karke hypotenuse calculate karte hain.

Result print karna: {BC:.2f} ka matlab hai result ko 2 decimal places tak round karna.


"""
import math  # Math library for sqrt()

# User se do perpendicular sides ka input lena
AB = float(input("Enter the length of AB: "))
AC = float(input("Enter the length of AC: "))

# Pythagorean theorem: BC^2 = AB^2 + AC^2
BC = math.sqrt(AB**2 + AC**2)

# Hypotenuse ka result dikhana
print(f"The length of BC (the hypotenuse) is: {BC:.2f}")
