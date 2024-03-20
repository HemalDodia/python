n=int(input("n=="))
num=n
Total=0
multi=1
while(n>0):
    rem=n%10
    Total=Total+rem
    multi=multi*rem
    n=n//10
    
if Total==multi:
    print("it is spy number")
else:
    print("it is not spy number")    
