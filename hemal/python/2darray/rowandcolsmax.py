a = [    
        [1, 2, 3],  
        [4, 5, 6],  
        [7, 8, 9]  
    ];  

for i in range(0,len(a[0])):
    max=a[i][0]
    for j in range(0,len (a)):
        if(max<a[i][j]):
            max=a[i][j]
    print("Max element of rows ",max)
                
 
for i in range(0,len(a[0])):
    max=a[0][i]
    for j in range(0,len (a)):
        if(max<a[j][i]):
            max=a[j][i]
    print("Max element of cols ",max)
                            