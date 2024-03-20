# total
# class demo:
#     def array(self):
#         self.a=[[23,34,45,34],[34,55,45,34,34]]
# class demo1(demo):     
#     def array1(self):
#             for i in range(0,len(self.a)):
#              for j in range(0,len(self.a[i])):
#               print(self.a[i][j],end=" ")      
#             self.total=0    
            
# class demo2(demo1):
#     def array2(self):                   
#             for i in range(0,len(self.a)):
#              for j in range(0,len(self.a[i])):
#                self.total+=self.a[i][j]
#             print("\ntotal sum of element is",self.total) 
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# # cross  max
# class demo:
#     def array(self):
#              self.a =[    
#                       [1, 22],  
#                        [34,8],   
#                     ]; 
# class demo1(demo):     
#     def array1(self):
#         max=self.a[0][0] 
#         for i in range(0,len(self.a[0])):
#          for j in range(0,len (self.a)):
#             if(i==j):
#              if(max<self.a[i][j]):
#                max=self.a[i][j]
#         print("cross max ",max)
# class demo2(demo1):
#     def array2(self):                
#         max=self.a[0][0] 
#         for i in range(0,len(self.a[0])):
#             for j in range(0,len(self.a)):
#                  if(i+j==len(self.a)-1):  
#                     if(max<self.a[i][j]):
#                         max=self.a[i][j]
#         print("cross max ",max)

# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# cross min
# class demo:
#     def array(self):
#              self.a =[    
#                       [1, 22],  
#                        [3,8],   
#                     ]; 
# class demo1(demo):     
#     def array1(self):
#         min=self.a[0][0] 
#         for i in range(0,len(self.a[0])):
#          for j in range(0,len (self.a)):
#             if(i==j):
#              if(min>self.a[i][j]):
#                min=self.a[i][j]
#         print("cross min ",min)
# class demo2(demo1):
#     def array2(self):            
#         min=self.a[0][1] 
#         for i in range(0,len(self.a[0])):
#             for j in range(0,len(self.a)):
#                  if(i+j==len(self.a)-1):  
#                     if(min>self.a[i][j]):
#                         min=self.a[i][j]
#         print("cross min ",min)

# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# crosssum
# class demo:
#     def array(self):
#              self.a =[    
#                       [1, 22],  
#                        [3,8],   
#                     ]; 
# class demo1(demo):     
#     def array1(self):
#         sum=0
#         for i in range(0,len(self.a[0])):
#          for j in range(0,len(self.a)):
#                 if(i==j ):
#                   sum=sum+self.a[i][j]
#         print("cross sum= ",sum)
# class demo2(demo1):
#     def array2(self):
#         sum=0
#         for i in range(0,len(self.a[0])):
#             for j in range(0,len(self.a)):
#                 if(i+j==len(self.a)-1):
#                     sum=sum+self.a[i][j]
#         print("cross sum= ",sum)
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# rowandcolsmax
# class demo:
#     def array(self):
#                self.a = [    
#                    [1, 2, 3],  
#                    [4, 5, 6],  
#                    [7, 8, 9]  
#                    ];  

# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a[0])):
#            max=self.a[i][0]
#            for j in range(0,len(self.a)):
#             if(max<self.a[i][j]):
#               max=self.a[i][j]
#            print("Max element of rows ",max)
           
# class demo2(demo1):
#     def array2(self):           
#         for i in range(0,len(self.a[0])):
#               max=self.a[0][i]
#               for j in range(0,len(self.a)):
#                 if(max<self.a[j][i]):
#                  max=self.a[j][i]
#               print("Max element of cols ",max)
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()

# rowandcolsmax
# class demo:
#     def array(self):
#                self.a = [    
#                    [1, 2, 3],  
#                    [4, 5, 6],  
#                    [7, 8, 9]  
#                    ];  

# class demo1(demo):     
#     def array1(self):
#         for i in range(0,len(self.a[0])):
#            min=self.a[i][0]
#            for j in range(0,len(self.a)):
#             if(min>self.a[i][j]):
#               min=self.a[i][j]
#            print("Min element of rows ",min)
           
# class demo2(demo1):
#     def array2(self):           
#         for i in range(0,len(self.a[0])):
#               min=self.a[0][i]
#               for j in range(0,len(self.a)):
#                 if(min>self.a[j][i]):
#                  min=self.a[j][i]
#               print("Min element of cols ",min)
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()


# rowandcolssum
# class demo:
#     def array(self):
#                self.a = [    
#                    [1, 2, 3],  
#                    [4, 5, 6],  
#                    [7, 8, 9]  
#                    ];  

# class demo1(demo):     
#     def array1(self):
#          self.rows=(len(self.a))     
#          self.cols=(len(self.a[0]))
       
#          for i in range(0,self.rows):
#           sumRow=0 
#           for j in range(0,self.cols):
#             sumRow = sumRow + self.a[i][j];  
#           print("Sum of " + str(i+1) +" row: " + str(sumRow))  

# class demo2(demo1):
#     def array2(self):
#          for i in range(0,self.rows):
#           sumcols=0 
#           for j in range(0,self.cols):
#             sumcols = sumcols + self.a[j][i];  
#           print("Sum of " + str(i+1) +" cols: " + str(sumcols))  
  
# obj=demo2()
# obj.array()
# obj.array1()
# obj.array2()