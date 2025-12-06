class Student:
    def __init__(self,name,contact):
        self.n=name
        self.c=contact
    def add_new(self,rollno):
        self.r=rollno
    def display(self):
        print(self.n,self.c,self.r,self.email)   

obj=Student("neeraj",1234)
obj.add_new(101)
obj.email='abc@gmail.com'
obj.display()
print(obj.n,obj.c,obj.email)
