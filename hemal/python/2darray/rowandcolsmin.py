a = [    
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ];  

for i in range(0,len(a[0])):
    min=a[i][0]
    for j in range(0,len (a)):
        if(min>a[i][j]):
            min=a[i][j]
    print("Minimum element of rows ",min)
                
 
for i in range(0,len(a[0])):
    min=a[0][i]
    for j in range(0,len (a)):
        if(min>a[j][i]):
            min=a[j][i]
    print("Minimum element of cols ",min)
                            