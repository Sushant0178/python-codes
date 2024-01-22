

# # class main():
# #     # def access(self):
# #     #     print("Accessing the variable")
# #     def __init__(self,name ,age):
# #         pass
# #         self.name = name
# #     #     self.age  = age 
# #     # def __str__(self) -> str:
# #     #     return f"{self.name} is {self.age} years old"
# #     def sus(self):
# #         print("hello my name is " + self.name)
# # m1 = main('John',20)
# # # a = m1.name

# # # print(a)

# # # print(m1.age)

# # m1.sus()
# # del m1
# # print("after deleting object")

# # try :
# #     print(m1.name)
# # except Exception as e :
# #     print(e)

# # class sushant():
# #     def __init__(self,name ,age):
# #         self.name = name
# #         self.age  = age

# # a = sushant("sushant",21)
# # del a.name
# # try:
# #     print(a.name)
# # except Exception as q:
# #     print(q)

# class person():
#     def __init__(self,fname ,lname):
#         self.name = fname
#         self.surname  = lname
#     def user_name(self):
#         print(self.name, self.surname)
    
# user = person("sushant","kokate")
# user.user_name()

# class student(person):
#     pass

# x = student("sagar", "shinde")
# x.user_name()

# class collage(student):
#     pass
# y = collage("anand", "patil")

# y.user_name()

# user.user_name()

# print(person.__bases__[0].__name__)



class sushant():
    def ok(self,name ,age ):
        self.name = name
        self.age = age
ssushant = sushant()
try:
    ssushant.ok('sushant',34)
except Exception as e:
    print("okkk")
print(ssushant.name ,ssushant.age)