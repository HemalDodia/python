# odd and even
# oddoreven = lambda n: 'odd' if n % 2 else 'even'
# print(oddoreven(int(input('enter number'))))  


# password check
# l, u, p, d = 0, 0, 0, 0
# s = input("enter password :-")
# check=lambda s: len(s) >=4 
# if(check(s)):
#  for i in s: 
#      if (i.isupper()):
#         l=1  
#      elif (i.islower()):
#         u=1 
#      elif (i.isdigit()): 
#          d=1
#      elif ( not i.isalnum()): 
#          p=1  
# if (l and u and p and d ==1):
#     print("Valid Password")
# else:
#     print("Invalid Password")          

# min and max

# a=[12,34,54,67,89]
# check=lambda a:len(0,a)
# min=a[0]
# max=a[0]
# for i in range(0,len(a)):
#     if min>a[i]:
#         min=a[i]
#     if max<a[i]:
#         max=a[i]
# print("min=",min)
# # print("max=",max)            


# asc and dsc

# a=[12,34,54,67,89]
# check=lambda a:len(0,a)
# for i in range(0,len(a)):
#     print('a',i,'=',a[i])
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i]>a[j]) :
#             temp=a[i]
#             a[i]=a[j] 
#             a[j]=temp  
# print('asc order print')
# for i in range(0,len(a)):
#     print(a[i])
# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         if(a[i]<a[j]) :
#             temp=a[i]
#             a[i]=a[j] 
#             a[j]=temp  
# print('dsc order print')
# for i in range(0,len(a)):
#     print(a[i])

# startingletterarraay
a=["creative","cdmi","abhishek","hemal"]
check= lambda a:len(a)
b = []
for i in range(0,len(a)) :
    print('a',i,'=',a[i])

for i in range(0,len(a)) :
    if (a[i][0]=="c") :
        b.append(a[i])
print(b)