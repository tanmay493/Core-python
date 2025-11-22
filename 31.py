# x='A'
print(ord(x))
print(ord(x)+1)
print(chr(ord(x)+1))
#-------------------
n=int(input("enter a no."))
ch=input("enter  starting character")
for i in range(n):
    print(ch)
    ch=chr(ord(ch)+1)
