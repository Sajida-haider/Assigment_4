"""
Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code for you which prompts the user to input the list one element at a time.

Task:
Aapko get_first_element(lst) function banana hai jo ek list ko parameter ke roop mein lega aur us list ka pehla element print karega. Yeh function tabhi call hoga jab list already user se input karke banayi gayi ho.

"""

def get_first_element(lst):
    # List ka pehla element print karna
    print(lst[0])

def main():
    # User se list ke elements lene ki process
    n = int(input("How many elements do you want to input? "))
    lst = []
    for i in range(n):
        element = input(f"Enter element #{i + 1}: ")
        lst.append(element)

    # List ko pass karna function mein
    get_first_element(lst)

if __name__ == "__main__":
    main()
    """
    Ek Simple Example:
Socho ke tum ek bucket me apples daal rahe ho, jab tak tum rukne ka signal nahi dete, bucket me apples girte rahenge.

🛠 Yahan bucket = lst hai aur apples = elem

Agar tum "apple" likho, woh list me chala jayega.

Agar tum "banana" likho, woh bhi list me chala jayega.

Agar tum enter daba do bina koi likhe, loop ruk jayega.

Step-by-Step Breakdown:

elem = input("Please enter an element or press enter to stop: ")
while elem != "":  # Jab tak elem khaali nahi hota, loop chalega
    lst.append(elem)  # List me value add karo
    elem = input("Please enter an element or press enter to stop: ")  # Phir se input lo
➡️ Jab tak user input deta rahega, list me values add hoti rahengi.
➡️ Jab user sirf enter daba dega, loop ruk jayega.

Aur Bhi Aasan Tarika:
🚀 Agar tum ise urdu bol chal me dekho to:


Jab tak user kuch likh raha hai,
    list me add karo.
Agar user enter daba de bina likhe,
    ruk jao.

    """

