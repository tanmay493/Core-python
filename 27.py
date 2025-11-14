s=input("enter any string")
v,c=0,0 ## ya hum aise bhi likh sakte hai v=c=0

for i  in s:
    if i in ('a','e','i','o','u','A','E','I','O','U'):
        v=v+1
    elif i=='':
        pass

    else:
        c=c+1    


print('v=',v)
print('c=',c)

