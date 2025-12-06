class Student:
    grad=10
    def __init__(self,name,rollno):
        self.n=name
        self.r=rollno

    @classmethod
    def update(cls,add):
        cls.grad=new

new=int(input("enter grad"))

obj=Student('neeraj',101)
print(Student.grad,obj.n,obj.r)
obj.update(11)
print(Student.grad,obj.n,obj.r)
