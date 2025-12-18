# For Loop
for i in range(5):
    print(i)

# Print numbers from 1 to 10

for i in range(1,11):
    print(i)

# print even numbers from 1 to 20

for i in range(2,21,2):
    print(i)

# print odd numbers from 1 to 20

for i in range(1,20,2):
    print(i)

# print any table

value=int(input("enter the number"))
for i in range(1,11,1):
    print(value,'*',i,'=',value*i)

num=int(input("enter the number"))
for i in range(1,11,1):
    print(num,'*',i,'=',num*i)

# print a plaendrome

s=input("enter the string")
rev=""
for i in range(len(s)-1,-1,-1):
    rev+=s[i]
if s==rev:
    print(s,"is a palendrome")
else:
    print(s,"is not a palendrome")


# print the sum of first 10 natural numbers

sum=0
for i in range(1,11):
    sum+=i
print("the sum of first 10 natural numbers is",sum)
