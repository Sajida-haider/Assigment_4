"""
Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]

Yeh program likhne ke liye aap ek loop ka use kar sakte hain jo har element ko 2 se multiply kare:


"""
def double_elements(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2
    return numbers

# Example usage:
numbers = [1, 2, 3, 4]
result = double_elements(numbers)
print(result)
"""
Explanation:
double_elements(numbers): Yeh function list numbers ko as argument leta hai.

Loop (for i in range(len(numbers))): Yeh loop list ke har element ko iterate karta hai.

numbers[i] *= 2: Yeh step har element ko 2 se multiply kar raha hai.

return numbers: Final doubled list return ki jaati hai.

Agar aap numbers = [1, 2, 3, 4] se start karte hain, to output hoga:
"""