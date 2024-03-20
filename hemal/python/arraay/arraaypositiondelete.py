a=[12,34,54,67,89]
for i in range(0,len(a)):
    print('a',i,'=',a[i])
pos=int(input('enter postion='))

for i in range (0,len(a)):
    if not(pos==i):
        print(a[i]) 
   
        