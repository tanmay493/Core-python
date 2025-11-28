# def add(*args):     #args is variable
    # print(args)
    # print(type(args))
# add(1,2,3,4,5,6,7,8,9)   
# --------------
def add(*n):
    sum=0
    for i in  n:
        sum=sum+i   
    return sum
x=add(1,2,3,4) 
print(x)       