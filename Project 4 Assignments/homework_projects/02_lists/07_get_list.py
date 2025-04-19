"""
Yeh program aapko values ko list mein add karne ke liye continuous input lene ko keh raha hai. Jab user enter press kare bina kuch type kiye, tab list ko print karna hai.

Yeh program kuch is tarah se likha jaa sakta hai
"""

def main():
    values = []  # Empty list to store user inputs

    while True:
        value = input("Enter a value: ")  # Ask user for input

        if value == "":  # If user presses enter without typing anything
            break  # Exit the loop

        values.append(value)  # Add the input to the list

    print("Here's the list:", values)  # Print the list when the loop ends


if __name__ == "__main__":
    main()

    """
    values = []: Ek empty list banai jaati hai jisme hum user ke inputs ko store karenge.

while True:: Yeh loop tab tak chalega jab tak hum manually ise break nahi karte.

value = input("Enter a value: "): Har bar user se input liya jaata hai.

if value == "":: Agar user ne kuch input nahi kiya aur bas enter press kiya, to loop break ho jaata hai.

values.append(value): Agar input diya gaya hai, to us value ko list mein add kar liya jaata hai.

print("Here's the list:", values): Jab loop khatam ho jaata hai, to puri list print ho jaati hai
"""
