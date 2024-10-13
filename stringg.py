# c = r"c:\user\pwd"
# #---------------------->
# c = "c:\user\pwd" 
# print(c)
# #                         #File "d:\codes\python-codes\stringg.py", line 1
# #                         #     c = "c:\user\pwd"
# #                         #         ^^^^^^^^^^^^^
# #                         # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
# #                         # PS D:\codes\python-codes> python -u "d:\codes\python-codes\stringg.py"
# #                         #   File "d:\codes\python-codes\stringg.py", line 1
# #                         #     c = "c:\user\pwd"
# #                         #         ^^^^^^^^^^^^^
# #                         # SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \uXXXX escape
# #                         # PS D:\codes\python-codes>

# # #----------------------->

# string= "sushant"
# rev_string = ''.join(reversed(string))
# print(rev_string)
# print(string)
# if string[0] or string[-1]== rev_string[-1] or rev_string[0]:
#     print("yes")
# else:
#     print("NOT")

# ok = "prajot pratap sing"

# print(len(ok))
# # rev_ok = ok[::-1]
# # print(rev_ok)
# line = []
# for i in ok :
    
#     line.append(i)
    
# tupleline = tuple(line)
# # print(tupleline)
# line.remove(" ")
# line.remove(" ")

# setline = set(line) #------------------------------------> set doest have any sequence
# setline.remove("p")
# # print(setline)

# # print(len(setline))
# # print(len(line))
# listsetline = list(setline)

# print(line)
# print(listsetline)
# print(len(line)-len(setline))

# print(ok.upper())
# ok=set(ok)
# print(type(ok))
# ok.remove(" ")
# print(len(ok))


# ok ="sush sushat"
# ok = tuple(ok)
# print(len(ok))
# print(ok)
# print(ok.count("s"))



# fint_words = "sushant"

# tuplefint_words = tuple(fint_words)
# a = str(input())
# if tuplefint_words.count(f"{a}") == 0:
#     print("not in string")
# else:
#     print("yes in string")
#     print(fint_words.count(a))

# rev= fint_words[::-1]
# j =rev.upper()
# print(rev)
# print(j)
# p= j[::-1]
# print(p)
# if len(j)==len(p):
#     if j[0] == p[-1]:
#         print("yes ")
#     else:
#         print("no")
# else:
#     print("dont have same lenght")



# def rev(s):
    
#     stringg =""
#     for i in s:
#         stringg = i + stringg
#     return stringg

# print(rev("sushant"))

a = "the way of speak"

# a = a[::-1]
a = a.upper()
a = a.replace(" ","")
a = tuple(a)
# print(a)

for i in a[0]:
    b = i
    
print(b)
