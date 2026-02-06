# Write a Python program that takes a dictionary as input and returns a new dictionary with the keys and values swapped.

n = int (input("Enter a number of key values pairs : "))
user_dict = {}
for i in range(n) :
    key = input("Enter key : ")
    value = input("Enter value : ")
    user_dict[key] = value
def swap_dict(input_dict):
    swapped_dict = {}
    for key, value in input_dict.items():
        swapped_dict[value] = key
    return swapped_dict
result = swap_dict(user_dict)
print(result)
