d={
    "name":"Abhinay",
    "age":21,
    (1,2):"tuple as key",
    (1,2,3):"tuple as key",
    True:1,
    0:False
}


# traversing through dictionary

for i in d:
    print(i)
    print(d[i])
    print(d["age"])


# adding new key value pair

d={
    1:"Abhinay",
    2:"Lakidi",
    3:"Python"
}

d[4]="Django"
print(d)
d["course"]="Backend Development"
print(d)
print(d[2])

# creating a dictionary using dict() function

l=[(1,'Yash'),('age',22),('COurse','java')]

d1=dict(l)
print(d1)

# Zip function to create dictionary

keys=['name','age','course']
values=['Abhinay',21,'Python']

d2=dict(zip(keys,values))
print(d2)

d3=(zip(keys,values))
for i in d3:
    print(i)

# enumerate function to create dictionary

values=['Abhinay',21,'Python']
d4=dict(enumerate(values,start=2))
print(d4)

d5={1:"one",2:"Two",3:"Three"}
k=d5.keys()
for i in k:
    print(i)

v=d5.values()
for i in v:
    print(i)

it=d5.items()
for i in it:
    print(i)

# updating the dictionary

d5.update({4:"Four"})
print(d5)

# Deletion 
# pop

d5.pop(4)
print(d5)

# popitem
d5.popitem()
print(d5)

d5.popitem()
print(d5)

# clear
d5.clear()
print(d5)

# del
# del d5
# print(d5) # this will give error as d5 is deleted

# copy
d6={1:"one",2:"Two",3:"Three"}  
d7=d6.copy()
print(d7)

# dictionary comprehension

d8=[(1,'Abhinay'),(2,'Lakidi'),(3,'Python')]
l3={x:y for (x,y) in d8}
print(l3)
l4={y:x for (x,y) in d8}
print(l4)

