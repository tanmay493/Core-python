age=int(input("enter a no"))
if 0<age<18:
    print("child")
elif 17<age<60:
    print("adult")   
elif 59<age<100:
    print("sr.citizen") 
elif age<0:
    print("pls enter age in +ve")   
else:
    print("please enter valid age")    
