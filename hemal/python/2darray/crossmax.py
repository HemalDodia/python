a = [    
        [1, 2],  
        [3,8],   
    ]; 
max=a[0][0] 
for i in range(0,len(a[0])):
    
    for j in range(0,len (a)):
        if(i==j):
         if(max,a[i][j]):
            max=a[i][j]
print("cross max ",max)
                
max=a[0][0] 
for i in range(0,len(a[0])):
    for j in range(0,len(a)):
        if(i+j==len(a)-1):  
            if(max<a[i][j]):
                max=a[i][j]
print("cross max ",max)
