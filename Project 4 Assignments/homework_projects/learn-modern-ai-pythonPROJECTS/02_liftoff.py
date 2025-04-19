""""
Yeh task spaceship ke countdown ka program banane ke liye hai. Tumhein countdown 10 se 1 tak print karna hai, aur uske baad Liftoff! print karna hai.

Steps:
Tum for loop ka use kar sakte ho jo 10 se 1 tak countdown karega.

range() function ka use karenge, lekin hum reverse counting karenge, isliye range(10, 0, -1) use karenge.

Loop ke baad Liftoff! print hoga.
"""
# Countdown program

# For loop to print countdown from 10 to 1
for i in range(10, 0, -1):
    print(i, end=" ")  # Prints numbers with space on the same line

# After countdown, print Liftoff!
print("Liftoff!")
