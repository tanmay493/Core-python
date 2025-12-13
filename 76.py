from abc import ABC,abstractmethod
class A(ABC):
    def dashboard(self):
        print("welcome to dashboard")
    @abstractmethod
    def login(self):
        pass
class B(A):
    def login(self):
        print("login sucessfully")
    
    
obj=A()
obj.login()