n=int(input("n=="))
i=n
sum=0
while(n!=0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
if(sum==i):
    print("palindrome")
else:
    print("not palindrome")     