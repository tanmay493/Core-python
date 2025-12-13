# private var
class A:
    __x=10
    def __show():
        print("from class A")
        print(A.__x)
class B(A):
    pass

obj=B()

print(dir(A))

# print(obj.__x)
# obj.__show()
# print(A.__x)
# A.__show(10)
print(A._A__x)