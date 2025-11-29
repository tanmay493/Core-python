# def decore():
#     def inner():
#         print("hello")

#     return inner


# x=decore()
# print(x)
# x()
#--------------------------
# 
# def abc(fun):
#     def inner(p,q):
#         p=p+5
#         q=q*2
#         fun(p,q)
#     return inner
# @abc
# def add(x,y):
#     print(x+y)
# add(10,20)


def decore(fun):
    def inner(x):
        for i in range(1,x+1):
            print(2*i-1)
    return inner
@decore
def even(n):
    for i in range(1,n+1):
        print(2*i)
n=int(input("enter no. of series"))  
even(n)                 


