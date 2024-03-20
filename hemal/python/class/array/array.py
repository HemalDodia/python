#1-> asc and dsc order
# class demo:
#     def array(self):
#         a=[12,34,54,67,89]
#         for i in range(0,len(a)):
#             print('a',i,'=',a[i])
#         for i in range(0,len(a)):
#             for j in range(i+1,len(a)):
#                 if(a[i]>a[j]) :
#                     temp=a[i]
#                     a[i]=a[j] 
#                     a[j]=temp  
#         print('asc order print')
    
#         for i in range(0,len(a)):
#          print(a[i])
#         for i in range(0,len(a)):
#             for j in range(i+1,len(a)):
#                 if(a[i]<a[j]) :
#                  temp=a[i]
#                  a[i]=a[j] 
#                  a[j]=temp  
#         print('dsc order print')
    
#         for i in range(0,len(a)):
#             print(a[i])
            
# b=demo()
# b.array()

            
# 2->arraaypositiondelete
# class demo:
#     def array(self):
#          a=[12,34,54,67,89]
#          for i in range(0,len(a)):
#           print('a',i,'=',a[i])
#          pos=int(input('enter postion='))

#          for i in range (0,len(a)):
#           if not(pos==i):
#             print(a[i]) 
            
# b=demo()
# b.array() 

           
# 3->startingletterarraay           
# class demo:
#     def array(self):
#           a=["creative","cdmi","abhishek","hemal"]
#           b = []
#           for i in range(0,len(a)) :
#            print('a',i,'=',a[i])

#           for i in range(0,len(a)) :
#             if (a[i][0]=="a") :
#              b.append(a[i])
#              print(b)      
# b=demo()
# b.array()             
             
# 4-> min and max                   
# class demo:
#     def array(self):
#          a=[12,34,54,67,89]
#          min=a[0]
#          max=a[0]
#          for i in range(0,len(a)):
#           if min>a[i]:
#             min=a[i]
#           if max<a[i]:
#             max=a[i]
#          print("min=",min)
#          print("max=",max)   
         
# b=demo()
# b.array()         
 
# add value at index   
      
a = [1,2,3,4,5,6]

print("Original List:")

for i in range(0,len(a)) :
    print('A',i,'=',a[i])

pos = int(input('Enter index = '))
val = int(input('Enter value = '))

for i in range(0,pos,-1) :
    a[i] = a[i-1]

a[pos] = val

for i in range(0,len(a)) :
    print(a[i])           
    
    
# array sum    
# class demo:
#     def array(self):
#           a=[12,34,54,67,89]
#           sum=0
#           for i in range(0,len(a)):
#             print("a[",i,"]=",a[i])
#             sum+=a[i]
#           print("sum=",sum)  
          
# b=demo()
# b.array()          