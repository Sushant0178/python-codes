# commen value

a = {1, 2, 3, 45, 5}
b = {1, 2, 3, 34, 455}
c = a.intersection(b)
print(c)
print(id(a), id(b), id(c))

# different values
diff = a.difference(b), b.difference(a)
print(diff)
# how to access elements from set
# we have to use loop
L = [1, 2, 3, 4, 5]
for i in L:
    print(i)
    print("hello")
print("student")


s = {1, 2, 3, 4, 4, 4, 4, 4}
for i in s:
    print(i, s)

# range : it is collective data type

# for i in range(1,11):
#     print(i)

for i in range(51):
    print(i)


for i in range(10, 21):
    print(i)


for i in range(1, 11):
    print(i*i)

for i in range(10, 21):
    print("square of", i, "is", i*i)

a = []
for i in range(50, 101):
    print(i)
    a.append(i)
print(a)

print("......................................................................")



# adding square in set from range function


s = set()
for i in range(1, 11):
    s.add(i*i)
print(s)
ls = [11,22,33,44,55]
for ls in  range(1,11,2):
    print(ls)
    
    
print("........................................................................")



for i in range(2,11,2):
    
        
    print(i)
    

print("........................................................................")


# PRINT ODD NUMBER FROM 12 - 20 

for i in range(13,21,2):
    print(i)


print("........................................................................")

lss= []
for i in range(50,101,2):
    lss.append(i)
print(lss)

print("........................................................................")

