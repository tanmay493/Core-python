fi=0
se=1

num=int(input("enter a no of fibonacci"))
for i in range(num):
    print(fi,end=" ")
    fi,se=se,fi+se
    
