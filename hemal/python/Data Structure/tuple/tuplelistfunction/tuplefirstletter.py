a=["creative","cdmi","abhishek","hemal"]
b = []
for i in range(0,len(a)) :
    print('a',i,'=',a[i])
    
for i in range (0,len(a)):
    b.append(a[i][0])
print(tuple(b))        