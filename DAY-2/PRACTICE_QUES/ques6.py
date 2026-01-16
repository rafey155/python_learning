# Write a program to add, subtract, multiply, and divide two numbers.
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
opp = input("Enter the operation which you want to perform : ")
if(opp == "+"):
    print(num1 + num2)
elif(opp == "-"):
    print(num1 - num2)
elif(opp == "*"):
    print(num1 * num2)
elif(opp == "/"):
    print(num1 / num2)
elif(opp == "%"):
    print(num1 % num2)
else:
    print("please fill the required fields:")
