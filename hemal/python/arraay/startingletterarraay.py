# a=["creative","cdmi","abhishek","hemal"]
# for i in range(0,len(a)):
#     print(a[i])
    
# b='a'
# # d=[item for item in a if item.startswith(b)] 
# print(b)
a=["creative","cdmi","abhishek","hemal"]
b = []
for i in range(0,len(a)) :
    print('a',i,'=',a[i])

for i in range(0,len(a)) :
    if (a[i][0]=="a") :
        b.append(a[i])
print(b)