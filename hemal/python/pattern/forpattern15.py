for i in range(1,6):
    for j in range(1,6):
        if(i+j==4 or i+j==8 or i-j==2 or j-i==2):
            print("*",end = " ")
        else:
            print(end = " ") 
    print()           
