# def make_palindrome(input_string):
#     return input_string + input_string[::-1]

# # Example usage:
# input_string = input()
# palindrome = make_palindrome(input_string)
# print(f"To make a palindrome from '{input_string}', add: {palindrome[len(input_string):]}")

input_str = input(":")


print(input_str[-1])
print(input_str[0])

if input_str[-1]==input_str[0]:
    print("The string is already palindrome.")
else:
    print("The string is not palindrome. Please try again with different characters.")
    add = input_str + input_str[::-1]
    print(add)
    