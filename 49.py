def add(x=0,y=0,z=0):
    return x+y+z

res=add()
print(res)
res1=add(10)
print(res1)
res2=add(10,20)
print(res2)
res3=add(10,20,30)
print(res3)

res4=add(10,20,30,40)#res4=add(10,20,30,40)
#TypeError: add() takes from 0 to 3 positional arguments but 4 were given
print(res4)