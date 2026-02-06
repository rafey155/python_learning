# Write a function that takes the input of three sides of Triangle ,and print whether it is equilateral,isosceles,Scalene

def cal_tri(a, b, c):
    
    if a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"

    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or a == c:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

result = cal_tri(a, b, c)
print(result)


