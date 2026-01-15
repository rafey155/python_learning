# WAP TO FINF THE GRESEST OF THREE NUMBER ENTERED BY THE USER
num1 = int(input("Enter first numer : "))
num2 = int(input("Enter second numer : "))
num3 = int(input("Enter third numer : "))
if (num1 > num2 and num1 > num3):
    print("first number is grtest :", num1)
elif(num2 > num1 and num2 > num3):
    print("Second number is gretest :", num2)
else:
    print("Third number is gretest :", num3)