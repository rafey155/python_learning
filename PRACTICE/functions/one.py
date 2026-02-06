def firstFunction():#this is the function without paremeter. 
    print("hell this is finction")

firstFunction()# this is the function call without agruments.

def greet(name, msg):
    print(name, msg)
greet("rafey", "hello")

# this is the default parementer function if the caller miss any one argumrnt it will pass the default agrumnet
def greet2(name, msg="heyy"):
    print(name, msg)
greet2("ayan")


# KEY WORDS ARGUMENTS 
def info(name, age, msg):
    print(msg, name, "your age is ", age)
info(msg ="hello", name = "rafey", age = 99)

# POSITIONAL ARGUMENTS
def add_num(x, y):
    print("X = ", x)
    print("Y = ", y)
    return x + y
print("The sum is ",add_num(5,6))

# MULTIPLE ARGUMRNST IN A function.
def sum_num(*args):
    print(args)
    total = 0
    for num in(args):
        total += num
    return total
print(sum_num(1,2,3,4,5))

# **kwargs
def fun(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key, "->", value)

print(fun(name = "rafey", age="99", gender ="male")) 


# returen type function
def add_num2 (a : int,  b : int ) -> int:
    return a+ b
print(add_num2(5,6))

# pass by vslue
num = 10
def modify(num):
    num += 1
    return num
modify(num)
print("original value = ",num)

# pass by reference 
my_li=[1,2,3]
def modi_li(li):
    my_li.append(5)
    return li
print("before calling function", my_li)

modi_li(my_li)

print("after calling function", my_li)

# lambda function
func = lambda x : x+10
print(func(5))
# --------------------------------------------------
add_num3 = lambda a,b: a+b
print(add_num3(2,4))