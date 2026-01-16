# Write a program to calculate the simple interest.
p = float(input("Enter the principal amount : "))
r = float(input("Enter the  rate of intrest :  "))
t = float(input("Enter the tenure : "))
total_amt = (p+r+t)
si =  ((p*r*t)/100)
print("The simple intrest (SI) of the amount is : ", si )
print("And the total amount is : ",total_amt + si)