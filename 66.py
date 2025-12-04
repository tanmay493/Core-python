class Student:
    def __init__(self,name,age,grad):
        self.n=name
        self.a=age
        self.g=grad
    def display(self):
        print(self.n,self.a,self.g)  

obj.display()
print(obj.n,obj.a,obj.g)