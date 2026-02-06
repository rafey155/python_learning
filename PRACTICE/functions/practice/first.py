# Write a program using a user defined function List_Mean() to calculate the mean of floating values stored in a list

numbers = [1.1,2.2,6.5,7.6,8.6,9.5,9.6,8.5,1.0]
def list_mean(numbers) :
    total = 0
    for n in numbers:
        total += n
    mean = total / len(numbers)
    return mean
result = list_mean(numbers)
print("the mean of the numbers are",result )