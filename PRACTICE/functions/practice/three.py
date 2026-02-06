# Write a program to make a simple calculator that can do addition, subtraction,multiplication and division using user defined functions

n1 = int(input("enter first number : "))
n2 = int(input("enter second number : "))
opp = input("Enter a opertaion to be perfomed : ")

def calc(n1, n2, opp):
    if opp == "+" :
        return n1 + n2
    elif opp == "-":
        return n1 - n2
    elif opp == "*":
        return n1 * n2
    elif opp == "/":
        if n2 != 0 :
            return n2 / n1
        else:
            print("cannot divide with zero : ")
    else:
        print("Invalid operation")
        
result = calc(n1,n2,opp)
print(result)   
  