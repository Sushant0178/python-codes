import function
l = [11,22,33,[2,3,4,5,[99,88,77],6],44,55,66]
l[3][4].append(999)
print(l)

l[3][4]=22
print(l)
l[3][2]=999
print(l)

l[3].insert(2,100)
print(l)
from function import add

add()