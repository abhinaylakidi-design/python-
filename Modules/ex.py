# Modules
# This module provides example functions for demonstration purposes.

# types of Modules:
# 1. Built-in modules
# 2. User-defined modules

# Examples of Built-in modules

import math
print("Square root of 16 is:", math.sqrt(16))
print(math.fabs(-7))
print(math.sin(90))
print(dir(math))

from random import random,randint,uniform,randrange,sample,choice,choices
print(random())

print(randint(1,10))

print(uniform(1,10))

print(randrange(10,100,2))

print(sample([1,2,3,4,5,6,7,8,9],3))

print(choice(['apple','banana','cherry']))
