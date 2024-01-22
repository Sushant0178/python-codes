from faker import Faker
import time
import random
fake = Faker()

uniq_name =set()
# a = random_namme 
# for i in range(100):
    # print(f"loading {} ")
   
for i in range(1):
    pass
    # time.sleep(1)
    # print(f" loading...............{i+1}....................")
while len(uniq_name)<100000:
    uniq_name.add(fake.name())
    
ran_name = list(uniq_name)
a = ran_name[:100000000000]
t = []
for i in a:

    t.append(i)
print("done")
print(t)

print(len(t))
for i in  t :
    rand_chose=random.choice(t)
    time.sleep(5)
    print(rand_chose)