"""Ek fruit shop hai.

Fruits ki prices ek dictionary mein store karni hain.

Program user se pooche ga:

"Kitne apples chahiye?"

"Kitne mangoes chahiye?"

etc...

User jitne fruits likhega usko multiply karega price se.

Sab fruits ka total add karke final bill dikhayega.

"""






def main():
    fruits = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_cost = 0

    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input(f"How many ({fruit_name}) do you want to buy?: "))
        total_cost += price * amount_bought

    print(f"Your total is ${total_cost}")


if __name__ == '__main__':
    main()
    
    """
    Output Example:
java
Copy
Edit
How many (apple) do you want?: 2
How many (durian) do you want?: 0
How many (jackfruit) do you want?: 1
How many (kiwi) do you want?: 0
How many (rambutan) do you want?: 1
How many (mango) do you want?: 3

Your total is $99.5



Summary:
Dictionary = Fruit name + price

For loop = Har fruit poocha

Input = User kitna lena chahta hai

Multiply = Quantity × Price

Total = Sab ka addition

Final Output = Total Bill


"""