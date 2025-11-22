n=int(input("enter a no"))
i,l=2,[]

while i<n:
    if n%i==0:
      l.append(i)
    i=i+1

print(l)
