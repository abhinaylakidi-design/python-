# loops in python
# Loops are used in programming to repeat a block of code multiple times until a certain condition is met.
# there are two main types in python:
# 1. for loop(for-each loop)
# 2. while loop(sentinel loop)

# syntax of for loop:

# for item in iterable:
#     # block of code to be executed for each item

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# syntax of while loop:
# while condition:
#     # block of code to be executed as long as the condition is true
count = 0
while count < 5:
    print("Count:", count)
    count += 1