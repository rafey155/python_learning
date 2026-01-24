# serch for the number X in the tupple using loop 
# [1,4,9,16,25,36,49,64,81,100]

tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Ehter a number you wnat to serch : "))
i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found at index ", i)
        break
    i += 1 
else:
    print("Number not found")


  