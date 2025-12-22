# string Methods and Operations

str1="Hello"

print(str1[0])  # H
print(str1[1])  # e

# Iteration
for i in str1:
    print(i)

print(len(str1))  # 5

# Concatenation
str2=" World"
str3=str1+str2  
print(str3)  # Hello World

# Repetition
str4=str1*3
print(str4)  # HelloHelloHello

# Membership
print('H' in str1)  # True
print('z' not in str1)  # True

# Slicing
print(str1[1:4])  # ell
print(str1[:3])   # Hel
print(str1[2:])   # llo
print(str1[-3:])  # llo
print(str1[::-1]) # olleH

# Built-in Functions
print(ord('A'))  # 65
print(chr(65))   # A
print(max(str1)) # o
print(min(str1)) # H
print(sorted(str1))  # ['H', 'e', 'l', 'l', 'o']
print(list(str1))  # ['H', 'e', 'l', 'l', 'o']
print(tuple(str1))  # ('H', 'e', 'l', 'l', 'o')
print(str(str1))  # Hello

# find
print(str1.find('e'))  # 1
print(str1.find('z'))  # -1

# rfind
print(str1.rfind('l'))  # 3
print(str1.rfind('z'))  # -1

# index
print(str1.index('e'))  # 1

# rindex
print(str1.rindex('l'))  # 3

# count
print(str1.count('l'))  # 2
print(str1.count('z'))  # 0

# replace
print(str1.replace('l', 'x'))  # Hexxo
print(str1.replace('z', 'x'))  # Hello

# strip
str5="  Hello World  "
print(str5.strip())  # "Hello World"
print(str5.lstrip())  # "Hello World  "
print(str5.rstrip())  # "  Hello World"

# split
print(str5.split())  # ['Hello', 'World']
print(str5.split('o'))  # ['  Hell', ' W', 'rld  ']

# join
print('-'.join(['Hello', 'World']))  # Hello-World
print(''.join(['H', 'e', 'l', 'l', 'o']))  # Hello

# case methods
print(str1.upper())  # HELLO
print(str1.lower())  # hello
print(str1.capitalize())  # Hello
print(str1.title())  # Hello
print(str1.swapcase())  # hELLO
print(str1.isupper())  # False
print(str1.islower())  # False
print(str1.istitle())  # True
print(str1.isalpha())  # True
print(str1.isdigit())  # False
print(str1.isalnum())  # True
print(str1.isspace())  # False
print(str1.startswith('He'))  # True
print(str1.endswith('lo'))  # True
print(str1.zfill(10))  # 00000Hello
print(str1.center(11, '*'))  # ***Hello***
print(str1.ljust(10, '-'))  # Hello-----
print(str1.rjust(10, '-'))  # -----Hello

# escape sequences
# This module provides functions to handle escape sequences in strings.
print("Hello,\nWorld!")  # New line escape sequence
print("Column1\tColumn2")  # Tab escape sequence
print("This is a backslash: \\")  # Backslash escape sequence
print("She said, \"Hello!\"")  # Double quote escape sequence
print('It\'s a beautiful day!')  # Single quote escape sequence



