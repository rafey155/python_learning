# Write a program to count even and odd numbers in a list.
ls = [1,2,3,4,5,6,8, 7,9,10,15]
even = []
odd = []
for i in ls:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("No of even elements :",even)
print( "No of odd elements :",odd)
    
    