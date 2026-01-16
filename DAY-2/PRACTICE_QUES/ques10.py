# Write a program to swap two numbers without using a third variable.
# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print("After swapping:")
print("a =", a)
print("b =", b)
