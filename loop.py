import random
a =[ 1,2,3,4,5,6]

print(a)
b =random.choice(a)
print(b)

if b == 1 :

    print("one")
elif b==2:
   print ("two")
else:
    print(a[1]+ a[2] +a[5])
    