"""
Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

The first even number is 0:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

Even numbers wo numbers hote hain jo 2 se divide ho jaayein bina remainder ke. Jaise:

✅ Tumhara goal:
Pehle 20 even numbers print karne hain.

"""
def main():
    for i in range(20):      # Yeh loop 0 se start hota hai, aur 19 tak jaata hai (20 baar chalta hai)
        print(i * 2)          # Har dafa i ko 2 se multiply karta hai (even number milta hai)
"""
range(20) ka matlab: i = 0 se 19 tak

Har i ko 2 se multiply karte hain: i * 2

Yani:

Pehli baar: 0 * 2 = 0

Doosri baar: 1 * 2 = 2

Teesri baar: 2 * 2 = 4

...

Aakhri baar: 19 * 2 = 38

🔁 Final Output:

0
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38


🧠 Full code:

def main():
    for i in range(20):
        print(i * 2)

if __name__ == "__main__":
    main()
Agar tum chaho to ye numbers ek hi line mein space ke sath bhi print karwa sakte ho:


def main():
    for i in range(20):
        print(i * 2, end=" ")  # end=" " ka matlab hai new line ki jagah space

if __name__ == "__main__":
    main()
Output:

0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38