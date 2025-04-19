"""
🔹 Is program ka kaam kya hai?
Yeh program:

User se age poochta hai (input() se).

Teen fictional countries ki voting age check karta hai:

Peturksbouipo → Voting age 16.

Stanlau → Voting age 25.

Mayengua → Voting age 48.

User ki age ko har country ki voting age se compare karta hai.

Bataata hai ke user vote kar sakta hai ya nahi.
"""
PETURKSBOUIPO_AGE : int = 16
STANLAU_AGE : int = 25
MAYENGUA_AGE : int = 48

def main():
    # User se age input lo
    user_age = int(input("How old are you? "))

    # Har country ki voting eligibility check karo
    if user_age >= PETURKSBOUIPO_AGE:
        print(f"You can vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is {PETURKSBOUIPO_AGE}.")
    
    if user_age >= STANLAU_AGE:
        print(f"You can vote in Stanlau where the voting age is {STANLAU_AGE}.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is {STANLAU_AGE}.")
    
    if user_age >= MAYENGUA_AGE:
        print(f"You can vote in Mayengua where the voting age is {MAYENGUA_AGE}.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is {MAYENGUA_AGE}.")

if __name__ == '__main__':
    main()
