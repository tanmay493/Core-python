class father:
    def home(self):
        print("home from father")
        # mother().home()
        # mother.home(self)
        
class mother:
    def home(self):
        print("home from mother")
        # father().home()
        # father.home(self) 
class child(mother,father): 
    def home(self):
        print("home from child")
        super().home()

obj=child()
obj.home()    