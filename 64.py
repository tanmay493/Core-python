class Student:
#     x=10
#     y=20
# obj=Student
# obj1=Student()    
# print(id(obj),id(obj1))
    def __init__(self):
        print("constructor called")
        print(id(self))
      
    def  __init__(self):
        print("hello")
        print(id(self))
obj1=Student()
obj1.__init__()        