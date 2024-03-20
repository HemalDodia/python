a=[12,34,54,67,89]
min=a[0]
max=a[0]
for i in range(0,len(a)):
    if min>a[i]:
        min=a[i]
    if max<a[i]:
        max=a[i]
print("min=",min)
print("max=",max)            
