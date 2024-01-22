db = {1: "tea", 2: "coffee", 3: "breadpakoda", 4: "poha", 5: "kachori", 6: "idli", 7: "dosa", 8: "appe"} 
db2 = {1: 12, 2: 20, 3: 25, 4: 22, 5: 10, 6: 30, 7: 45, 8: 30}
l = []
q = []
"""
l=[1,7,2,4]
l[i]3
l[0]---->1---->db[l[0]]---->tea------>
l[1]---->7---->db[l[i]]----->dosa
k[2]---->2
l[3]---->4----db[4]
"""
print("-"*65)
print("\t\t\tHotel Rajwadi")
print("-"*65)
while True:
    print(""" 
            1.tea              5.kachori
            2.coffee           6.idli
            3.breadpakoda      7.dosa     
            4.poha             8.appe
            
            """)

    print("-"*65)
    item = int(input("Enter item no= "))
    quantity = int(input("enter no of item= "))
    l.append(item)
    q.append(quantity)
    ch = input("Do you want to continue.(y/n)= ")
    sum = 0

    if ch == 'n':
        print("-"*90)
        print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(
            "Items", "Quantity", "Price", "Total"))
        print("-"*90)
        for i in range(len(l)):
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(
                db[l[i]], q[i], db2[l[i]], q[i]*db2[l[i]]))
            print("-"*90)
            sum = sum+(q[i]*db2[l[i]])
        break
print("Total Amount without GST =", sum)
print("Total Amount with GST =", int((8/100)*sum+sum))
print("Thank You ! \n Visit Again...")
