
# a=lambda x,y,z:2*x+y+z
# print(a(1,2,3))

# x=lambda x,y:x if x>y else y
# print(x(5,10))

# x=lambda age:'child' if 0<age<18 else('adult' if 17<age<60 else('senior' if 59<age else('invalid age')))
# age=int(input("enter age"))
# print(x(age))

# x=lambda n:'even' if n%2==0 else None
# n=int(input("enter no."))
# print(x(n))

# x=lambda n:n**2
# n=int(input("enter a no"))
# print(x(n))

# x=lambda p,q:p+q
# print(x(5,10))

# n=int(input ("enter a no"))
# x=lambda n:[i for i in range(1,n+1)]
# print(x(n))

# n=int(input("enter no."))
# x=lambda
from functools import reduce
l=[1,2,3,4,5]
# print(list(map(lambda n:n**2,l)))
# print(list(filter(lambda n : 'even'if n%2==0 else None,l)))
print((reduce(lambda x,y: x+y ,l,0)))

