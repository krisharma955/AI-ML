#functions -> block of code that perform a specific task

name = input("Enter your Name: ") #fxn definition
def sayHello(name):
    print("Hello,", name)
sayHello(name) #fxn call

#Sum of two numbers
def sum(a, b): #a,b - parameters
    return a + b
print(sum(2,1)) #arguments are passed on fxn call

#Average of three numbers
def avg(a, b, c):
    return (a + b + c) / 3
print(avg(1,2,3))

#default parameter values
def product(a, b = 3):
    return a * b
print(product(5))

#Lambda functions -> used for small expressions (tasks)
# used in higer order fxns
sum = lambda a,b,c: a+b+c
print(sum(1,2,3))

#Factorial of n
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac *= i
    return fac
print(factorial(5))