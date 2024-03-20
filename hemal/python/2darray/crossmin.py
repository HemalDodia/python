a = [    
        [1,2],  
        [3,4],   
    ]; 
min=a[0][0] 
for i in range(0,len(a[0])):
    
    for j in range(0,len (a)):
        if(i==j):
         if(min>a[i][j]):
            min=a[i][j]
print("cross min ",min)
                
min1=a[0][1] 
for i in range(0,len(a[0])):
    for j in range(0,len(a)):
        if(i+j==len(a)-1):  
            if(min1>a[i][j]):
                min1=a[i][j]
print("cross min ",min1)
