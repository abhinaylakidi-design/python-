# Functions 
# A function is a block of reusable code that performs a specific task.
#  Functions help in organizing code, improving readability, and reducing redundancy.
#  In Python, functions are defined using the `def` keyword followed by the function name and parentheses.

# types of functions:
# 1. Built-in functions
# 2. User-defined functions

# Example of a user-defined function

def greet():
    print("Hello, welcome to Python functions!")
greet()

# Function with parameters/arguments

def num(number):
    if number % 2 == 0:
        print(number,"is even")
    else:
        print(number,"is odd")
num(5)
num(10)

# Function with return statement
def add(a,b):
    return a+b
result=add(5,10)
print("Sum is:",result) 

# Function with multiple return values

def maths(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    return sum,sub,mul
print(maths(10,5))

# Function with default parameter value

def greet(name="Guest"):
    print("Hello",name)
greet()
greet("Abhinay")

# two types of arguments
# 1. Positional arguments
# 2. Keyword arguments

# Positional arguments

def info(name,age):
    print("Name:",name)
    print("Age:",age)
info("Abhinay",21)
info("Lakidi",22)

# Keyword arguments
def info(name,age):
    print("Name:",name)
    print("Age:",age)
info(age=21,name="Abhinay")
info(name="Lakidi",age=22)

# positional only arguments
def info(name,/,age):
    print("Name:",name)
    print("Age:",age)
info("Abhinay",21)
# info(name="Lakidi",age=22) # This will raise an error

# Keyword only arguments
def info(*,name,age):
    print("Name:",name)
    print("Age:",age)
info(name="Abhinay",age=21)
# info("Lakidi",22) # This will raise an error

# Mixed arguments

def sample(a,b,/,c,d,*,e,f):
    print(a,b,c,d,e,f)
sample(1,2,3,4,e=5,f=6)

# Variable-length positional arguments

def add(*args):
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3))
print(add(10,20,30,40,50))

# Variable-length keyword arguments

def info(**kwargs):
    for i in kwargs.values():
        print(i)

info(name="Abhinay",age=21,course="Python")
info(city="New York",country="USA")

# Nested functions
# A function defined inside another function

def outer():
    def inner():
        print("This is the inner function")
    inner()
    print("This is the outer function")
outer()

# First-class functions
# Functions that can be treated like any other variable

def greet():
    return "Hello, welcome to Python functions!"    
message=greet
print(message())

# callback functions

def greet(name):
    return "Hello " + name
def call_func(func, name):
    return func(name)
print(call_func(greet, "Abhinay"))

# Decorator functions

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper
@decorator
def say_hello():
    print("Hello!")
say_hello()

# lambda functions
# Anonymous functions defined using the lambda keyword

add=lambda a,b:a+b
print(add(5,10))

