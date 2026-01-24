tup = [1,4,9,16,25,36,49,64,81,100, 49, 49, 49]
num = int(input("Enter a number : "))
idx = 0
for i in tup:
    if(num == i) :
        print("Number Found at index : -> ", idx)
    idx += 1
else:
    print("End of loop") 