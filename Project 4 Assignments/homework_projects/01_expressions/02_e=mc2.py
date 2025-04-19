"""
Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

Here's a sample run of the program (user input is in bold italics):

Enter kilos of mass: 100

e = m * C^2...

m = 100.0 kg

C = 299792458 m/s

8.987551787368176e+18 joules of energy!


Ye program Einstein ke mass-energy formula E = m * C^2 ko use karke energy calculate karta hai. Har dafa user se mass (kg) input leta hai aur uska equivalent energy (joules) print karta hai.

"""
# Einstein's mass-energy equation calculator

# Speed of light in meters per second (m/s)
C = 3.0e8  # 300,000,000 m/s

while True:
    try:
        # User se mass input lena (kg)
        mass = float(input("Mass (kg) daalain: "))

        # Energy calculate karna
        energy = mass * C**2

        # Result print karna
        print(f"Equivalent Energy: {energy:.2e} Joules\n")

    except ValueError:
        print("Ghalat input! Sirf numbers daalain.\n")
