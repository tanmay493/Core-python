#Single-level Inheritance
class Parent:
    x=10
    def home(self):
        print("from parent class")
class Child(Parent):
    pass
obj=Child()
print(obj.x)
obj.home()        

