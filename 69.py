class Student:
    def __init__(self):
        x=10        #local varaiable
        print(x)
    def new(self):
        y=20
        z=y+10
        print(z)
        # print(x)
obj=Student()
obj.new()            
