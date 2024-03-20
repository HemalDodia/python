a = [    
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ];  
sum=0
for i in range(0,len(a[0])):
    for j in range(0,len(a)):
        if(i==j ):
            sum=sum+a[i][j]
print("cross sum= ",sum)
sum=0
for i in range(0,len(a[0])):
    for j in range(0,len(a)):
        if(i+j==len(a)-1):
            sum=sum+a[i][j]
            
print("cross sum= ",sum)
