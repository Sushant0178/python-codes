""""
type of programming 


1)
seq progarm.
2)
fun. program
3)
oop

"""


#  1)functional programming

""""
function defination 

functing calling 

"""

# addition of two numbers
def add():
    a = eval(input("Enter the number "))
    b = eval(input("enter the second number "))
    d = a+b
    print(d)
# substraction of two number 

def sub():
    a = eval(input("Enter the number "))
    b = eval(input("enter the second number "))
    d = a-b
    print(d)

# wap to print multi. of two number


def multi():
    a = eval(input("Enter the number "))
    b = eval(input("enter the second number "))
    d = a*b
    print(d)
# create a function for lenth of string


def sushant():
    str = input("enter the string")
    count = 0
    for i in str:
        count = count+1
    print(count)

# create a function for "aeiou"

def vol():
    a = input("enter the string:")
    b = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    c = ""
    d = 0
    for i in range(len(a)):
        if a[i] in b:
            c = c+a[i]
            d = d + 1
    print(d)

    print(c) 
    

### global scope/space
### local scope/space

"""
"""
X = 100
Y =50
def fun1():
    a = 10 
    b = 20
    print("local scope variable",a,b)
print("global scope variable",X,Y)

"""
WE CAN ACCESS GLOBAL SCOPE DATA WITHIN GLOBAL SCOPE


WE CAN ACCESS LOCAL SCOPE DATA WITHIN LOCAL SCOPE

"""

X = 100
Y =50
def fun2():
    a = 10 
    b = 20
    
    print("GLOBAL scope variable IN LLOCAL SCOPE",X,Y)  #WE CAN ACESS GLOBAL SCOPE DATA WITHIN LOCAL SCOPE 
#fun()
print("global scope variable",X,Y)

X = 100
Y =50
def fun3():
    global x # FOR CHANGE WE HAVE TO DO IT 
    a = 10 
    b = 20
    x = X+1 #WE CAN NOT CHANGE GLOBA;L SCOPE DATA IN LOCAL SCOPE -----------> WE CAN ACCESS BUT WE CAN NOT CHANGE IT WITH OUT GLOBAL FUNCTION 
    #WE HAVE TO DO 
    
# print(a)# we can not access local scope data within global scope data  ---------> "a" is not defined

c_name = "TCS"
location = "pune"
def details():
    e_name= "sushant"
    department= "HR"
    salary = 500000
    em_id= 11
    
# print(f"""{c_name}
#           ,{location}_____________
#       Name:-{e_name}              |
#                                   |                       |        
#       id:-{em_id}                 | - #----> NameError: name 'e_name' is not defined. Did you mean: 'c_name'? :- because the dta from local scope can not accessble in global scope 
#       department:-{department}    |
#       salary:-{salary}____________|
                      
#       """)

#  TO SOLVE THIS PROBLEM WE HAVE TO STORE THE FUNCTION IN VARIABLE |
                                                            
def ok():
    a = 100
    b = 200
    return a ,b# ----------> RETIRN STATEMENT OF THE FUNCTION WHATEVER YOU WRITE AFTER THE RETURN STATMENT THAT WAS NOT CONSIDERED 
    print("OK") #-------> THIS WILL NOT RUN
d ,c= ok()
e = ok()
print(d)
print(e)
