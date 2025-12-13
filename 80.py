# polymorphism
class A:
    def sound(self):
        print("hello")
class B:
    def sound(self):
        print("Hi")        

# l=[A,B]
# for i in l:
#     i.sound('x')   
                 
l=[A(),B()]
for i in l:
    i.sound()                 