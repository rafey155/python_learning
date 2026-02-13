print("Programe to find the factorial of a number: ")
num = int(input("Enter the number : "))
def find_fact(num):
    fact = 1
    for i in range (1, num+1):
        fact = fact * i
    return fact

result = find_fact(num)
print(result) 

        

