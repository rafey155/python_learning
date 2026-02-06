# Write a Python program to print the Fibonacci series up to n terms using a function
rng = int(input("Enter the length of series: "))

def fib (rng):
    a, b = 0, 1
    for i in range(rng):
        print(a, end=" ")
        a = b
        b = a + b

fib(rng)

    