"""
Humein ek function get_last_element(lst) likhna hai jo:
✅ Ek list (lst) ko input le
✅ Uska sabse aakhri (last) element print kare
✅ List khaali nahi hogi (kam az kam ek element zaroor hoga)

"""
lst = ["apple", "banana", "cherry"]
print(lst[-1])  # Output: cherry
lst[-1] ka matlab hai last element. Toh output "cherry" hoga.

Different lists banai:

fruits = ["apple", "banana", "cherry"]

marks = [99, 85, 77, 92, 88]

one_item = [100]

Har list ka last element function se print karwaya:

get_last_element(fruits) → cherry

get_last_element(marks) → 88

get_last_element(one_item) → 100

