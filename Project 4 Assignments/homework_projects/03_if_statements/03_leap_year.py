"""
Yeh code leap year ko check karta hai. Leap year woh hota hai jisme February ke mahine mein 29 din hote hain (normal saal mein 28 din). Iska purpose yeh hai ke humare calendar ko astronomical year ke saath match kiya jaaye. Leap year ko calculate karne ke liye 3 conditions hain:

Leap Year ka Rule:
Saal 4 se divide ho:

Agar ek saal 4 se divide hota hai, toh woh leap year ho sakta hai, lekin hum next steps pe bhi check karte hain.

Saal 100 se divide ho:

Agar saal 100 se divide hota hai, toh woh leap year nahi ho sakta, lekin ek aur special case hai:

Saal 400 se divide ho:

Agar saal 400 se divide hota hai, toh phir woh leap year ho sakta hai, even though woh 100 se divide hota hai.


Step-by-step Explanation:
Pehle code 4 se divide karne ki check karta hai. Agar sahi hota hai toh next step pe jata hai.

Phir 100 se divide hone ki condition check karta hai. Agar yeh condition sahi hoti hai, toh phir next step pe jata hai.

Agar 400 se divide hota hai, toh leap year hai. Agar 400 se divide nahi hota, toh leap year nahi hota.

Example:
2020:

2020 ko 4 se divide ho sakta hai.

2020 ko 100 se divide nahi hota (condition fail).

Result: Leap year hai!

1900:

1900 ko 4 se divide ho sakta hai.

1900 ko 100 se divide ho sakta hai.

Lekin 1900 ko 400 se divide nahi hota.

Result: Leap year nahi hai!

2000:

2000 ko 4 se divide ho sakta hai.

2000 ko 100 se divide ho sakta hai.

2000 ko 400 se divide ho sakta hai.

Result: Leap year hai!
"""

def main():
    # User se year input lete hain
    year = int(input('Please input a year: '))

    # Leap year check karna
    if year % 4 == 0:  # Agar year 4 se divide hota hai
        if year % 100 == 0:  # Agar year 100 se bhi divide hota hai
            if year % 400 == 0:  # Agar year 400 se divide hota hai
                print("That's a leap year!")  # Leap year
            else:  # Agar year 400 se divide nahi hota
                print("That's not a leap year.")  # Not a leap year
        else:  # Agar year 100 se divide nahi hota
            print("That's a leap year!")  # Leap year
    else:  # Agar year 4 se divide nahi hota
        print("That's not a leap year.")  # Not a leap year

# Program start hota hai
if __name__ == '__main__':
    main()

