# arraayascanddsc
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
          
          
# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a)):
#             print('a',i,'=',self.a[i])
#             for i in range(0,len(self.a)):
#              for j in range(i+1,len(self.a)):
#               if(self.a[i]>self.a[j]) :
#                 temp=self.a[i]
#                 self.a[i]=self.a[j] 
#                 self.a[j]=temp  
#         print('asc order print')
#         for i in range(0,len(self.a)):
#                print(self.a[i])
    
# class demo2(demo): 
#     def array2(self):
#             for i in range(0,len(self.a)):
#               for j in range(i+1,len(self.a)):
#                if(self.a[i]<self.a[j]) :
#                 temp=self.a[i]
#                 self.a[i]=self.a[j] 
#                 self.a[j]=temp  
#             print('dsc order print')
#             for i in range(0,len(self.a)):
#              print(self.a[i])       
# obj=demo1()
# obj1=demo2()
# obj.array()
# obj.array1()
# obj1.array()
# obj1.array2()


# arraayminandmax
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#         self.min=self.a[0]
#         for i in range(0,len(self.a)):
#            if self.min>self.a[i]:
#             self.min=self.a[i]
#         print("min =",self.min)
   
# class demo2(demo):
#     def array2(self):
#         self.max=self.a[0]
#         for i in range(0,len(self.a)):
#             if self.max<self.a[i]:
#              self.max=self.a[i]
#         print("max=",self.max)
   
# obj=demo1()
# obj1=demo2()
# obj.array()
# obj.array1()
# obj1.array()
# obj1.array2()

# arraaypositiondelete
# class demo:
#     def array(self):
#            self.a=[12,34,54,67,89]
# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a)):
#          print('a',i,'=',self.a[i])
        
# class demo2(demo):
#     def array2(self):
#         self.pos=int(input('enter postion='))
#         for i in range (0,len(self.a)):
#          if not(self.pos==i):
#           print(self.a[i]) 

# obj=demo1()
# obj1=demo2()
# obj.array()
# obj.array1()
# obj1.array()
# obj1.array2()

# startingletterarraay
# class demo:
#     def array(self):
#            self.a=["creative","cdmi","abhishek","hemal"]
#            self. b = []
# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a)):
#           print('a',i,'=',self.a[i])
         
# class demo2(demo1,demo):
#     def array2(self):        
#         for i in range(0,len(self.a)) :
#             if (self.a[i][0]=="c") :
#                 self.b.append(self.a[i])
#         print(self.b)       
# obj=demo1()
# obj1=demo2()
# obj.array()
# obj.array1()
# obj1.array()
# obj1.array2()