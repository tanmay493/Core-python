def factorial(a):
    ans=1
    for i in range(1,num+1):
        ans*=i
    return ans

num=int(input("enter a no"))
answer=factorial(num)
print(answer)    
