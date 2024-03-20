a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))

if(a<b and a<c):
    if(b<c):
        min,mad,max=a,b,c
    else:
       min,mad,max=a,c,b   
elif(b<a and b<c):
    if(a<c):
        min,mad,max=b,a,c
    else:
       min,mad,max=b,c,a
else:
    if(a<b):
        min,mad,max=c,a,b
    else:
       min,mad,max=c,b,a
       
       
print("$ $ Ascending print $ $") 
       
print(min)               
print(mad)  
print(max) 

if(a>b and a>c):
    if(b>c):
        min,mad,max=a,b,c
    else:
       min,mad,max=a,c,b   
elif(b>a and b>c):
    if(a>c):
        min,mad,max=b,a,c
    else:
       min,mad,max=b,c,a
else:
    if(a>b):
        min,mad,max=c,a,b
    else:
       min,mad,max=c,b,a
       
print("$ $ dsc print $ $") 
     
       
print(min)               
print(mad)  
print(max)  