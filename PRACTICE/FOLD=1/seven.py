# Write a program to check whether a string is a palindrome.
str1 = "12343219"
str2 = str1
str2 = str1[::-1] #[::-1] means start from end and move backward.
if (str2 == str1 ):
    print("palendrome")
else:
    print("not palendrome")