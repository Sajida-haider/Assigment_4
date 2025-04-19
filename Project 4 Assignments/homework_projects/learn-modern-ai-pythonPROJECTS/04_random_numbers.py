""""
Tumhein ek aisa program banana hai jo:

✅ 1 se 100 ke darmiyan 10 random numbers print kare
✅ Har dafa jab tum program chalao, to alag alag numbers aayein
✅ Saare numbers ek hi line mein print hoon
"""
import random

for i in range(10):
    print(random.randint(1, 100), end=' ')

"""
import random ➤ Python ka random module use kar rahe hain

for i in range(10) ➤ Loop 10 baar chalega

random.randint(1, 100) ➤ Har baar ek random number dega

end=' ' ➤ Iska matlab hai ke print new line na kare, sab numbers ek hi line mein
"""