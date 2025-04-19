
"""
Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.


Yeh raha ek simple Python ka code jo feet ko inches mein convert karega:
"""
def feet_to_inches(feet):
    return feet * 12

# Example usage
feet = float(input("Enter feet: "))
inches = feet_to_inches(feet)
print(f"{feet} feet is equal to {inches} inches.")
