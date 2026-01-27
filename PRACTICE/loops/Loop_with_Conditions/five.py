ls = [1,2,3,4,5,6,8,7,9,10,15, 70]
n = int(input("Enter a number: "))

for i in range(len(ls)):
    if ls[i] == n:
        print("Number found at index:", i)
        break
else:
    print("Number is not present in the list")
