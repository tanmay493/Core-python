# x=range(1,100)
# print(list(x))
# print(id(list(x)))

def natural_no(n):
    i=1
    while i<=n:
        yield i
        i=i+1
x=int(input("enter a no"))        
res=natural_no(x)
# print(res)
# print(next(res))
# print(next(res))
# print("hello")
# print(next(res))

# for i in range(5):
#     print(next(res))
#     # print("hello")
# for i in range(10):
#     print(next(res))  
for _ in range(10):
    try:
        print(next(res))
    except StopIteration:
        print("all elements are iterated,i.e,collection is empty")    
        break


    
