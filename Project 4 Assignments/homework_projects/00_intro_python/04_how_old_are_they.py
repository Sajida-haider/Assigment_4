

"""
Yeh program har dost ki age ko calculate karega aur output ko sahi format mein print karega:
"""

def main():
    anton: int = 21  # Anton ki age 21 hai
    beth: int = 6 + anton  # Beth Anton se 6 saal bari hai
    chen: int = 20 + beth  # Chen Beth se 20 saal bara hai
    drew: int = chen + anton  # Drew ki age Chen + Anton ke barabar hai
    ethan: int = chen  # Ethan ki age bhi Chen ke barabar hai

    # F-string ka istemal karke print karna
    print(f"Anton is {anton}")
    print(f"Beth is {beth}")
    print(f"Chen is {chen}")
    print(f"Drew is {drew}")
    print(f"Ethan is {ethan}")

# Ye part program ko run karega
if __name__ == '__main__':
    main()
