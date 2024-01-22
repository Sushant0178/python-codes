
# global scope/space
# local scope/space

"""



"""
X = 100
Y = 50


def fun1():
    a = 10
    b = 20                                #-----------------------------WE CAN ACESS THE GLOBLE DATA FROM THE GLOBAL SCOPE 
    print("local scope variable", a, b)


print("global scope variable", X, Y)

"""
WE CAN ACCESS GLOBAL SCOPE DATA WITHIN GLOBAL SCOPE


WE CAN ACCESS LOCAL SCOPE DATA WITHIN LOCAL SCOPE

"""

X = 100
Y = 50


def fun2():
    a = 10
    b = 20

                                                         #---------------------> WE CAN ACESS GLOBAL SCOPE DATA WITHIN LOCAL SCOPE
    print("GLOBAL scope variable IN LLOCAL SCOPE", X, Y)


# fun()
print("global scope variable", X, Y)

X = 100
Y = 50


def fun3():
    global x  # FOR CHANGE WE HAVE TO DO IT
    a = 10
    b = 20
    x = X+1  # WE CAN NOT CHANGE GLOBA;L SCOPE DATA IN LOCAL SCOPE -----------> WE CAN ACCESS BUT WE CAN NOT CHANGE IT WITH OUT GLOBAL FUNCTION
    # WE HAVE TO DO

# print(a)# we can not access local scope data within global scope data  ---------> "a" is not defined

def info():
    name = "sushant"
    location = "pune"
    
# print(f"""{name}
#           ,{location}----> NameError: name 'e_name' is not defined  'c_name'? :- because the dta from local scope can not accessble in global scope___________|
                      
#       """)

#  TO SOLVE THIS PROBLEM WE HAVE TO STORE THE FUNCTION IN VARIABLE |

def ok():
    a = 100
    b = 200
    return a, b  # ----------> RETIRN STATEMENT OF THE FUNCTION WHATEVER YOU WRITE AFTER THE RETURN STATMENT THAT WAS NOT CONSIDERED
    print("OK")  # ----------> THIS WILL NOT RUN


d, c = ok()  # ---------------> WE CAN ADD MULTIPLE DATA BY ","
e = ok()
print(d)  # |-----------------> WE CAN PRINT SEPREATE DATA FROM CALLING THAT VARIABLE
print(e)  # |
