# total
# class demo:
#     def array(self):
#         self.a=[[23,34,45,34],[34,55,45,34,34]]
# class demo1(demo):     
#     def array1(self):
#             for i in range(0,len(self.a)):
#              for j in range(0,len(self.a[i])):
#               print(self.a[i][j],end=" ")      
#             total=0        
#             for i in range(0,len(self.a)):
#              for j in range(0,len(self.a[i])):
#                total+=self.a[i][j]
#             print("\ntotal sum of element is",total) 
# obj=demo1()
# obj.array()
# obj.array1()

# cross  max
# class demo:
#     def array(self):
#              self.a =[    
#                       [1, 22],  
#                        [3,8],   
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
                
#         max=self.a[0][0] 
#         for i in range(0,len(self.a[0])):
#             for j in range(0,len(self.a)):
#                  if(i+j==len(self.a)-1):  
#                     if(max<self.a[i][j]):
#                         max=self.a[i][j]
#         print("cross max ",max)

# obj=demo1()
# obj.array()
# obj.array1()
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
                
#         min=self.self.a[0][1] 
#         for i in range(0,len(self.a[0])):
#             for j in range(0,len(self.a)):
#                  if(i+j==len(self.a)-1):  
#                     if(min>self.a[i][j]):
#                         min=self.a[i][j]
#         print("cross min ",min)

# obj=demo1()
# obj.array()
# obj.array1()

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
#         sum=0
#         for i in range(0,len(self.a[0])):
#             for j in range(0,len(self.a)):
#                 if(i+j==len(self.a)-1):
#                     sum=sum+self.a[i][j]
#         print("cross sum= ",sum)
# obj=demo1()
# obj.array()
# obj.array1()

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
#         for i in range(0,len(self.a[0])):
#               max=self.a[0][i]
#               for j in range(0,len(self.a)):
#                 if(max<self.a[j][i]):
#                  max=self.a[j][i]
#               print("Max element of cols ",max)
# obj=demo1()
# obj.array()
# obj.array1()

# rowandcolsmin
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
#         for i in range(0,len(self.a[0])):
#               min=self.a[0][i]
#               for j in range(0,len(self.a)):
#                 if(min<self.a[j][i]):
#                  min=self.a[j][i]
#               print("Min element of cols ",min)
# obj=demo1()
# obj.array()
# obj.array1()


# rowandcolssum
class demo:
    def array(self):
               self.a = [    
                   [1, 2, 3],  
                   [4, 5, 6],  
                   [7, 8, 9]  
                   ];  

class demo1(demo):     
    def array1(self):
         rows=(len(self.a))     
         cols=(len(self.a[0]))
       
         for i in range(0,rows):
          sumRow=0 
          for j in range(0,cols):
            sumRow = sumRow + self.a[i][j];  
          print("Sum of " + str(i+1) +" row: " + str(sumRow))  


       
         for i in range(0,rows):
          sumcols=0 
          for j in range(0,cols):
            sumcols = sumcols + self.a[j][i];  
          print("Sum of " + str(i+1) +" cols: " + str(sumcols))  
  
obj=demo1()
obj.array()
obj.array1()