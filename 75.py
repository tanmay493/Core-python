# hierarchial inheritance
class A:
    def home(self):
        print("from class A")
class B(A):
    def home(self):
        print("from class B")
        super().home()   
        # C.home(self)     
class C(A):
    def home(self):
        print("from class C")  
        super().home()  

obj=C()
obj.home()