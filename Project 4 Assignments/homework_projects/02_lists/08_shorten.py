"""
Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. 
If lst is already shorter than MAX_LENGTH you should leave it unchanged.
 We've written a main() function for you which gets a list and passes it into your function once you run the program.
  For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.
  """"
MAX_LENGTH : int = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)

def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)

if __name__ == '__main__':
    main()

"""
Question ka maksad kya hai?
Tumhein ek shorten(lst) function likhna hai jo:

List ke aakhir se elements hataata hai (pop karta hai),

Aur har hataya gaya element print karta hai,

Jab tak list mein sirf 3 elements reh jaayein (yaani MAX_LENGTH = 3).

Agar list mein pehle se 3 ya usse kam elements hain to kuch nahi karna.

🔸 MAX_LENGTH : int = 3
Yeh ek constant hai — iska matlab hai list mein sirf 3 items rehne dene hain, baaki hata do.

🔹 Ab function shorten(lst) ka kaam kya hai?

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        last_elem = lst.pop()
        print(last_elem)
➤ Roman Urdu mein samjhao:
Jab tak list ki length MAX_LENGTH se zyada hai,

tab tak:

last item list se hatao (pop()),

aur usse print karo.

Example:

lst = ["apple", "banana", "cherry", "mango", "grape"]
To shorten(lst) karega:


grape
mango
Aur list ban jaayegi: ["apple", "banana", "cherry"]

🔸 get_lst() kya karta hai?
Ye user se list banwata hai — ek ek karke input leke.

Roman Urdu:

User se ek ek item poochta hai.

Jab user khali input de (press enter), to input lena band kar deta hai.

Aur us waqt tak jo items liye gaye woh list bana kar return kar deta hai.

🔸 main() kya karta hai?
get_lst() se list leta hai.

shorten(lst) ko call karta hai"""
