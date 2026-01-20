# Take 5 numbers from the user, store them in a list, and print the list.
numbers = []

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)

print("The list is:", numbers)

