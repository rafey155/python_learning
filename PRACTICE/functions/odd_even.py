print("Checking odd and even using function")
num = int(input("Enter the number : "))
def check(num):
    if num == 0:
        return "zero cant be check for even or odd"
    elif num % 2 == 0:
        return "The number is Even"
    else:
        return "The number is odd"
result = check(num)
print(result)

