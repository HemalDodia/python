n=int(input("n=="))
i=n
a=1
sum=0
while(n!=0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
if(sum==i):
    print("palindrome")
else:
    print("not palindrome") 
if(i%2==0):      
     print("even number")    
else:
       print("odd number")