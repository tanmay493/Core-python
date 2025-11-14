h=int(input("enter hindi marks"))
if (0<=h<=100):
    e:int(input("enter english marks"))
    if (0<=e<=100):
        m:int(input("enter maths marks"))
        if(0<=m<=100):
            avg=((h+e+m)/3)
            if 0<=avg<=34:
                print("fail")
                
            elif(35<=avg<=44):
                print("3rd division")
            elif(45<=avg<=59):
                print("2nd division") 
            else:
                print("1st division")     


            
else:
    print("pls enter marks bw 0 and 100")

else:
    print("pls enter marks bw 0 & 100")

 

else:
    print("pls enter marks bw 0 and 100")
