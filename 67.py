class Student:
    def __init__(self,name,contact):
        self.n=name
        self.c=contact
    def add_new(self,rollno):
        self.r=rollno
    def display(self):
        print(self.n,self.c,self.r)    
