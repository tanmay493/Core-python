x=int(input("enter a year"))
if((x%4==0 and x%100!=0 ) or x%400==0):
    print(f'given year {x} is leap year')
 
else:
    print(f'given year{x} is not leap year')

       
