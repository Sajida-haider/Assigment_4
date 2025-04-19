"""
 aap ne ek aisa program banana hai jo dictionary ka use kar ke phonebook banaye.
 Matlab:
→ Dictionary = key-value pairs
→ Phonebook = Name (key) → Number (value)
 
 """
 # Phonebook using Dictionary

# Creating phonebook
phonebook = {
    "Ali": "03001234567",
    "Sara": "03111234567",
    "Ahmed": "03211234567"
}

# Print phonebook
print("Phonebook:")
for name, number in phonebook.items():
    print(name, ":", number)

# Search any contact
name = input("Enter name to search: ")

if name in phonebook:
    print(f"{name}'s number is: {phonebook[name]}")
else:
    print("Contact not found.")

# Add new contact
new_name = input("Enter new name: ")
new_number = input("Enter number: ")
phonebook[new_name] = new_number

print("Updated Phonebook:")
print(phonebook)
"""
Output:

Phonebook:
Ali : 03001234567
Sara : 03111234567
Ahmed : 03211234567

Enter name to search: Sara
Sara's number is: 03111234567

Enter new name: Zain
Enter number: 03005551234

Updated Phonebook:
{'Ali': '03001234567', 'Sara': '03111234567', 'Ahmed': '03211234567', 'Zain': '03005551234'}
Summary:
Is program mein:

Phonebook banaya dictionary se

Contact search kiya

New contact add kiya

Update dikhaya
"""
