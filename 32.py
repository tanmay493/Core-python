n=int(input("enter a no"))
for i in range(n):
    ch='A'
    for j in range(n):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()    