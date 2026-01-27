# Write a program to reverse a number.

n = input("Enter a number : ")
print(n[::-1])

# using while loop 

m = int(input("Enter a number : "))
rev = 0 
while m > 0:
    dig = m % 10
    rev = rev * 10 + dig
    m = m // 10
print(rev)