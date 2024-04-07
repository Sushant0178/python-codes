
# my_list = []

# # Take 5 user inputs and append them to the list
# for i in range(5):
#     user_input = input(f"Enter value {i + 1}: ")
#     my_list.append(user_input)

# # Append the names list to the my_list
# names = [
#     "Alice", "Bob", "Charlie", "David", "Eva",
#     "Frank", "Grace", "Henry", "Ivy", "Jack",
#     "Katherine", "Leo", "Mia", "Nathan", "Olivia",
#     "Patrick", "Quinn", "Rachel", "Samuel", "Tara",
#     "Ulysses", "Victoria", "Walter", "Xena", "Yasmine",
#     "Zane",
# ]

# my_list.extend(names)

# # Print the combined list
# print("Combined List:", my_list)

# # Iterate through the list and check for names containing 's'
# for item in my_list:
#     if "s" in item:
#         print(f"{item} contains 's'")
#     else:
#         print(f"{item} does not contain 's'")
        
for i in range(2):
    print("i"+"a")
print("\n\n")

j=0

def my_list(num):
    global j
    return num+j

print(my_list(5))
j=7
print(my_list(8))

while j < len(my_list):
        print(my_list[j])
        
        