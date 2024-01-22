# WAP to print 1 - 10
i =1
while i <=10:
    print(i)
    i =i+1
    
# WAP to print odd number between 11 to 20 
i =11
while i <=20:
    print(i)
    i =i+2
#WAP a program to print the squres of  odd numbers 1 to 20 

i =1
while i <=20:
    print("the squre of",i,"is",i*i)
    i =i+2
    
#WAP to print table of 15
i = 15
while i <=150:
    print(i)
    i = i+15
    
# WAP same with reverse 

i = 150 
while i >=15:
    print(i)
    i = i-15
    
# WHILE LOOP WITH REAK STATEMENT 
count = 0
while True:
    print("hello")
    count = count+1
    print(count)
    c = input("do you want to continue:(y|n)")
    if c =="n":
        break
    pass

# wap to print factorial to number 
num = int(input("a number :"))

i = 1
while num >=1:
    print(i)
    i=i*num
    num =num -1
    
# with for loop
result =1
numm = 5
for i in range(1,numm+1):
    
    result = result*i
    
print(result)

