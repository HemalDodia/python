# arraayascanddsc
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
          
          
# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a)):
#             print('a',i,'=',self.a[i])
#         for i in range(0,len(self.a)):
#           for j in range(i+1,len(self.a)):
#              if(self.a[i]>self.a[j]) :
#                 temp=self.a[i]
#                 self.a[i]=self.a[j] 
#                 self.a[j]=temp  
#         print('asc order print')
#         for i in range(0,len(self.a)):
#              print(self.a[i])
#         for i in range(0,len(self.a)):
#           for j in range(i+1,len(self.a)):
#               if(self.a[i]<self.a[j]) :
#                 temp=self.a[i]
#                 self.a[i]=self.a[j] 
#                 self.a[j]=temp  
#         print('dsc order print')
#         for i in range(0,len(self.a)):
#          print(self.a[i])

# obj=demo1()
# obj.array()
# obj.array1()

# arraayminandmax
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#         min=self.a[0]
#         max=self.a[0]
#         for i in range(0,len(self.a)):
#            if min>self.a[i]:
#             min=self.a[i]
#            if max<self.a[i]:
#             max=self.a[i]
#         print("min=",min)
#         print("max=",max)            

# obj=demo1()
# obj.array()
# obj.array1()
       
# arraaypositiondelete
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a)):
#          print('a',i,'=',self.a[i])
#         pos=int(input('enter postion='))

#         for i in range (0,len(self.a)):
#          if not(pos==i):
#           print(self.a[i]) 

# obj=demo1()
# obj.array()
# obj.array1()
    
# arraaysum
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#      sum=0
#      for i in range(0,len(self.a)):
#       print("a[",i,"]=",self.a[i])
#       sum+=self.a[i]
#       print("sum=",sum)       
  
# obj=demo1()
# obj.array()
# obj.array1()


# startingletterarraay
class demo:
    def array(self):
           self.a=["creative","cdmi","abhishek","hemal"]
class demo1(demo):     
    def array1(self):
        b = []
        for i in range(0,len(self.a)) :
         print('a',i,'=',self.a[i])
        for i in range(0,len(self.a)) :
            if (self.a[i][0]=="c") :
                b.append(self.a[i])
        print(b)       
obj=demo1()
obj.array()
obj.array1()