# first_vr = int(input("Enter frist number:"))
# secound_vr = int(input("Enter secound number:"))
# third_vr = int(input("Enter third number:"))
# # addicton of three numbers
# add_of_three_number = first_vr + secound_vr + third_vr
# print(add_of_three_number)

# Get the size of the multiplication table from the user
table_size = int(input("Enter the size of the multiplication table: "))

# Create a nested loop to generate the multiplication table
for i in range(1, table_size + 1):
    for j in range(1, table_size + 1):
        print(i * j, end='\t')
    print()
