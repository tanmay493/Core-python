class A:
    x=10 #public var
    def show(self):
        print("from class A")
        print(A.x)
class B(A):
    pass

obj=B()
# print(obj.x)
# obj.show()
# print(A.x)
A.show(2)
