# multi-level inheritance
class grandparent:
    def home(self):
        print("home from grandparent")
class parent(grandparent):
    def home(self):
        print("home from parent")
        super().home()
class child(parent):
    def home(self):
        print("home from child")
        super().home()       

obj=child()   
obj.home() 
# obj1=parent()
# obj1.home()            