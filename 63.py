class Student:
    def __init__(self):
         print("constructor called")
         print(id(self))
obj1=Student
print(id(obj1),id(Student))

obj2=Student()
print(id(obj2),id(Student))
         
