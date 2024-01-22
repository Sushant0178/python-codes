
import time 
    

def ok(inn):
    r = ""
    # inn = int(input(":"))
    for i in range(inn,0,-1):
        r = r+"* "
        print(r)
    
    # for i in range(0,6,1):
    #     for j in range(0,i+1):
        
    #        print("*",end=" ")
    #     print()
    


    # for i in range(6,0,-1):
    #     for j in range(1,i+1):
    #         print("*",end=" ")
    #     print()
i =0     
while True:
    ok(50) 
    time.sleep(5)
    i = i+1

    