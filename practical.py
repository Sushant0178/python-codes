
from faker import Faker
fake = Faker()

uniq_name =set()
# a = random_namme 
while len(uniq_name)>100000:
    print(uniq_name.add(fake.name()))
    
ran_name = list(uniq_name)
    
print(ran_name[10])


# for i in range(5):
    # in_put = input(f"enter the value {i+1} : ")
    # res = list.append(in_put)
    # pass
# for i in list:
#     pass
#     res = list.append(i)
# print(list)

# inp = int(input())
# for a in list :
#     if len(a) == inp:
#         print(f"{a} the lenth is  {len(a)}")
#     else:
#         continue
    


