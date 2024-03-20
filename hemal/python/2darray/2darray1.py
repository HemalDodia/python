a=[[23,34,45,34],[34,55,45,34,34]]
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        print(a[i][j],end=" ")
       

total=0        
for i in range(0,len(a)):
    for j in range(0,len(a[i])):
        total+=a[i][j]
        print("total sum of element is",total)      
        
