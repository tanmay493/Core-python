class Student:
    '''This is demo class''' #doc string
#     pass
# print(dir(Student))
# # dir-directory
# print(Student.__doc__) #__doc__ is magic variable

    x=10
    y=20
    def show():
        print("hello")
# print(Student.__dict__)
#print(dir(Student))        
print(id(Student))
obj=Student()
print(id(obj))
obj2=Student
obj3=Student
print(id(obj2),id(obj3))