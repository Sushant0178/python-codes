print("-"*100)
print("""
                               | welcome to infotech | 
      """)

print("-"*100)
user_name = "sushant"
user_pass = "0178"


while True:
    print("""
            
            
         please log in
            
        """)

    new_user_name = input("Enter the user name :")
    new_user_pass = input("Enter the your password:")

    if new_user_name == user_name and new_user_pass == user_pass:
        break
    else:
        print('wrong username and/or pass')



while True:
    main_info = {}
    print("-"*100)
    print("""
          welcome to infotech
          
          """)
    print("-"*100)
    print("""
          
          What you want to do
          
          """)
    print("-"*100)
    while True:
        print("""
            
            1:add
            2:update
            3:delete
            4:view
            
            """)
        choice = int(input("Enter the choise :"))
        if choice == 1:
            name = input("Enter the name:")
            id = int(input("Enter the id number:"))
            mobile_number = int(input("Enter your mobile number:"))
            post = input("Enter your post :")
            main_info[id] = {"name": name, "Employee id": id,
                             "mobile number": mobile_number, "post": post}

        elif choice == 4:

            print("-"*100)
            print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(
                "employee name", "employee id", "employee mo.number", "post"))
            print("-"*100)
            for id, main_infoo in main_info.items():
                print("-"*100)
                print("|{:^20}|{:^20}|{:^20}|{:^20}|".format(
                    main_infoo["name"], main_infoo["Employee id"], main_infoo["mobile number"], main_infoo["post"]))
        elif choice == 2:
            update_id = int(input("enter employee id which u wanna update:"))
            if update_id in main_info:
                updated_info = main_info[id]
                print("name", updated_info["name"])
                print("Employee id", updated_info["Employee id"])
                print("mobile number", updated_info["mobile number"])
                print("post", updated_info["post"])

                print("""
                      
                      Enter what your new innformation
                    
                       """)
                name = input("Enter the new name:")
                number = input("Enter the new number:")
                post = input("Enter your post:")
                updated_info["name"] = name
                updated_info["mobile number"] = number
                updated_info["post"] = post
            else:
                print("this is not a valid entry")
        elif choice == 3:
            delete_id = int(input("enter employee id to be deleted:"))
            del (main_info[delete_id])
        
