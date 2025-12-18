i=1
while i<11:
    print(i)
    i+=1
else:
    print("loop is ended")



for i in range(1,11):
    print(i)
else:
    print("for loop is ended")

# pass

for i in range(1,11):
    if i>=1 and i<=5:
        pass
    else:
        print(i)
print('loop is completed')

# continue

for i in range(1,6):
    if i==1:
        continue
    if i==2:
        continue
    if i==3:
        print(i)
        pass
    if i==4:
        continue
    print('loop completed')
print('loop ended')


# break

for i in range(1,6):
    if i==1:
        print('loop started')
        continue
    if i==2:
        break
    if i==3:
        print(i)
        pass
    if i==4:
        continue
    print('loop completed')
print('loop ended')

for i in range(1,11):
    if i%3==0:
        continue
    print(i)