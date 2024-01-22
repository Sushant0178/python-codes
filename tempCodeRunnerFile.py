
list = [
    "Alice", "Bob", "Charlie", "David", "Eva",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Katherine", "Leo", "Mia", "Nathan", "Olivia",
    "Patrick", "Quinn", "Rachel", "Samuel", "Tara",
    "Ulysses", "Victoria", "Walter", "Xena", "Yasmine",
    "Zane",
    # Repeat the names to make a list of 100
    "Alice", "Bob", "Charlie", "David", "Eva",
    "Frank", "Grace", "Henry", "Ivy", "Jack",
    "Katherine", "Leo", "Mia", "Nathan", "Olivia",
    "Patrick", "Quinn", "Rachel", "Samuel", "Tara",
    "Ulysses", "Victoria", "Walter", "Xena", "Yasmine",
    "Zane",
    # Repeat more names as needed
]
# for i in range(5):
    # in_put = input(f"enter the value {i+1} : ")
    # res = list.append(in_put)
    # pass
# for i in list:
#     pass
#     res = list.append(i)
# print(list)

inp = int(input())
for a in list :
    if len(a) == inp:
        print(f"{a} the lenth is  {len(a)}")
        
    else:
        print(f"there is no words for lenth{inp}")
