"""
Is program ka kaam yeh hai ke yeh aap se aapki height puchta hai aur yeh check karta hai ke aap rollercoaster ride ke liye minimum height se zyada lambi hain ya nahi. Agar aap minimum height se upar hain to yeh aapko batata hai ke aap ride kar sakte hain, warna yeh kehta hai ke aap ride nahi kar sakte.

Program ka explanation Roman Urdu mein:
MINIMUM_HEIGHT: Yeh ek variable hai jo minimum height define karta hai, yani 50 units. Yeh woh height hai jo rollercoaster ride ke liye required hai.

Input loop: Program bar bar aap se height puchta hai jab tak aap kuch input nahi dete (agar aap bas Enter dabate hain to program band ho jata hai).

Height check: Agar aap valid height input karte hain:

Agar aapki height minimum height ke barabar ya usse zyada hoti hai, to program aapko kehta hai: "You're tall enough to ride!".

Agar aapki height kam hoti hai, to program yeh kehta hai: "You're not tall enough to ride, but maybe next year!".

Error handling: Agar aap kuch galat input karte hain (jaise koi letter ya string) to program aapko kehta hai: "Please enter a valid number for height.".

"""
MINIMUM_HEIGHT = 50  # arbitrary units

def main():
    while True:
        # User se height puchna
        height_input = input("How tall are you? ")

        # Agar user ne kuch nahi input kiya (Enter press kiya)
        if height_input == "":
            print("Goodbye!")
            break  # Program ko band kar dena

        try:
            # Height ko float mein convert karna
            height = float(height_input)

            # Agar user ki height minimum height se zyada hai
            if height >= MINIMUM_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            # Agar user ne koi galat cheez daali (jaise letter)
            print("Please enter a valid number for height.")

# Program start
if __name__ == '__main__':
    main()
