# f=open('n7.txt','x+')
# print(f.tell())

# f=open('n7.txt','r+')
# print(f.tell())

# f=open('n7.txt','w+')
# print(f.tell())

# f=open('n7.txt','a+')
# print(f.tell())

# f=open('n1.txt','r+')
# print(f.tell())
# data =f.read(10)
# print(data)

f=open('n1.txt','rb+')
print(f.tell())

# data=f.read(10)
# print(data)

f.seek(20)
print(f.tell())

f.seek(-1,2)
print(f.tell())

f.seek(-7,2)
data=f.read()
print(data)