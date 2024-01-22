string = input("enter the string :")

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
r =""
for i in range(len(string)):
    
    if string[i] in vowels:
        r=r+string[i]
# print(r) print(r)


    # print(string[i]) 
    
    
# a = string[1:len(string)] 


    r = r+"*"
    