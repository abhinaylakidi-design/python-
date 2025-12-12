# print the numbers from 1 to 10 using while loop

# i=1

# while i<11:
#     print(i)
#     i+=1

# print the numbers from 10 to 1 using while loop

num1=10

while num1>0:
    print(num1)
    num1-=1

# print the even numbers from 0 to 10

num2=2
while num2<11:
    print(num2)
    num2+=2

# Print the of string

name="Abhinay"
i=0
while i<len(name):
    print(name[i])
    i+=1

# print the right angle triangle using stars

i=1
while i<6:
    print('* '*i)
    i+=1

# print the triangle reverse

i=5
while i>0:
    print('* '*i)
    i-=1

# print the a triagle

i=1
while i<6:
    print(' '*(5-i)+'* '*i)
    i+=1


# print the sum of first n natural numbers

n=5
i=1
sum=0
while i<=n:
    sum=sum+i
    i+=1
print("The sum is:",sum)