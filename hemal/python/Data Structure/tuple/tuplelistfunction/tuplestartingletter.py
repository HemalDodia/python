a=["creative","cdmi","abhishek","hemal"]
b = []
for i in range(0,len(a)) :
    print('a',i,'=',a[i])

for i in range(0,len(a)) :
    if (a[i][0]=="c") :
        b.append(a[i])
print(tuple(b))