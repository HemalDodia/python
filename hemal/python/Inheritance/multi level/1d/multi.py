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
# class demo2(demo1):
#     def array2(self):
#           for i in range(0,len(self.a)):
#            print(self.a[i])       
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# arraayminandmax
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#         self.min=self.a[0]
#         self.max=self.a[0]
#         for i in range(0,len(self.a)):
#            if self.min>self.a[i]:
#             self.min=self.a[i]
#            if self.max<self.a[i]:
#              self.max=self.a[i]
# class demo2(demo1):
#     def array2(self):
#             print("min =",self.min)
#             print("max=",self.max)
   
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()


# arraaypositiondelete
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a)):
#          print('a',i,'=',self.a[i])
#         self.pos=int(input('enter postion='))
        
# class demo2(demo1):
#     def array2(self):
#         for i in range (0,len(self.a)):
#          if not(self.pos==i):
#           print(self.a[i]) 

# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# arraaysum
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#      self.sum=0
#      for i in range(0,len(self.a)):
#       print("a[",i,"]=",self.a[i])
#       self.sum+=self.a[i]
      
# class demo2(demo1):
#     def array2(self):           
#           print("sum=",self.sum)
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# startingletterarraay
class demo:
    def array(self):
           self.a=["creative","cdmi","abhishek","hemal"]
class demo1(demo):     
    def array1(self):
        self. b = []
        for i in range(0,len(self.a)):
          print('a',i,'=',self.a[i])
         
class demo2(demo1):
    def array2(self):        
        for i in range(0,len(self.a)) :
            if (self.a[i][0]=="c") :
                self.b.append(self.a[i])
        print(self.b)       
obj=demo2()
obj.array()
obj.array1()
obj.array2()