l=[1,2,3,4,5]
# print(l)

x=iter(l)
# print(x)
# for i in x:
#     print(i)
for i in range(2):
    print(next(x))    

for i in range(3):
    print(next(x)) 