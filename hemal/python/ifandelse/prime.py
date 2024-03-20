n=int(input("enter any number=="))
i=1
prime=0
while i<=n:
    if(n%i==0):
        prime+=1
    i+=1

if (prime == 2):
    print("it is prime number")
else:
    print("it is not prime number")            
