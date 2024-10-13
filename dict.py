dict = {"masala":'spicy',"ginger":'sushant',"green":"mild"}
dict["ginger"]="zesty"


for chai in dict:
    # print(chai,dict[chai])
    pass

for key,value in dict.items():
    print(key,value)
    
new_dict= dict.fromkeys(dict,"sushant" )
print(new_dict)