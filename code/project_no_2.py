# student management system

student = {1:{"name":"jay","roll no":1,"city":"pune","percentage":89}}
print("-"*100)
print("\t\t\t\t\tstudent management system")
new_dic ={}

print("-"*100)
while True:
      print("""
            1.Add
            2.Display
            3.update
            4.delete
            """)

      ch = int(input("enter your choise :"))

      if ch==1:
            name = input("Enter the name :")
            print("-"*100)
            
            roll = int(input("enter your roll number :"))
            print("-"*100)  
            city = input("Entet your city :")
            print("-"*100)  
            per = int(input("Entet your percentage :"))  
            print("-"*100)  
            student[1]["name"]=name
            student[1]["roll no"]= roll
            student[1]["city"]=city
            student[1]["percentage"]=per
            print("|{:^20}|{:^20}|{:^20}".format("Name","Roll number","City","percentage"))
            print("-"*100)
            for i in student:
                  print("|{:^20}|{:^20}|{:^20}".format(student[1]["name"],student[1]["roll no"],student[1]["city"],student[1]["percentage"]))
            
            