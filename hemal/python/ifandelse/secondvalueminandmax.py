a=int(input("a=="))
print(a)
b=int(input("b=="))
print(b)
c=int(input("c=="))
print(c)
d=int(input("d=="))
print(d)
     

           
if a<b:
     m=a
     s=b
else :
     m=b
     s=a

if c<m:
     s=m
     m=c
elif c<s :
     s=c
     
if d<m:
     s=m
     m=d
elif d<s:
     s=d
     
print("second smallest number=",s)               
     
             
  
if a>b:
     m=a
     s=b
else :
     m=b
     s=a

if c>m:
     s=m
     m=c
elif c>s :
     s=c
     
if d>m:
     s=m
     m=d
elif d>s:
     s=d
     
print("second biggest number=",s)               
     
          