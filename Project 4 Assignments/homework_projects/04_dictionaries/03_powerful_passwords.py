"""
Program banana hai jo password ko safe way mein store kare using hashing — aur phir login check kare.
"""
# Hashing library import
from hashlib import sha256

# Function to hash password
def hash_password(password):
    return sha256(password.encode()).hexdigest()

# Login check karne wala function
def login(email, stored_logins, password_to_check):
    # Check karega kya email ka password match krta hai
    if email in stored_logins:  # check email exists
        if stored_logins[email] == hash_password(password_to_check):
            return True  # password correct
    return False  # wrong email or password


# Main program
def main():
    # Emails aur hashed passwords store kiye hue hain
    stored_logins = {
        "sajida@gmail.com": hash_password("sajida123"),
        "ali@gmail.com": hash_password("ali321"),
        "noor@gmail.com": hash_password("noor456")
    }

    email = input("Enter your Email: ")
    password = input("Enter your Password: ")

    # Login function call
    if login(email, stored_logins, password):
        print("Login Successful!")
    else:
        print("Invalid Email or Password!")


# Program start from here
if __name__ == '__main__':
    main()


"""
Enter your Email: sajida@gmail.com
Enter your Password: wrongpass
Invalid Email or Password!


Easy Explanation:
Line	Kaam
hash_password()	password ko hash mein change karta
stored_logins	email → hashed password save
login()	email & password check karta
main()	user se email/password le raha
Result	Password match? → Success / Fail
"""