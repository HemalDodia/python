# 1-> total sum
# class demo: 
#    def array(self):
#          a=[[23,34,45,34],[34,55,45,34,34]]
#          for i in range(0,len(a)):
#           for j in range(0,len(a[i])):
#            print(a[i][j],end=" ")
       

#           total=0        
#           for i in range(0,len(a)):
#            for j in range(0,len(a[i])):
#             total+=a[i][j]
#             print("total sum of element is",total)  
            
# b=demo()
# b.array()  
              
# 2-> crossmax       
# class demo:
#     def array(self):
#             a = [    
#                  [1, 2],  
#                  [3,8],   
#             ]
#             max=a[0][0] 
#             for i in range(0,len(a[0])):
    
#                for j in range(0,len (a)):
#                  if(i==j):
#                   if(max<a[i][j]):
#                    max=a[i][j]
#             print("cross max ",max)
                
#             max=a[0][0] 
#             for i in range(0,len(a[0])):
#                for j in range(0,len(a)):
#                  if(i+j==len(a)-1):  
#                     if(max<a[i][j]):
#                       max=a[i][j]
#             print("cross max ",max)
# b=demo()
# b.array()

# 3-> crossmin                          
# class demo:
#     def array(self):
#             a = [    
#                  [12, 22],  
#                  [3,8],   
#             ]
#             min=a[0][0] 
#             for i in range(0,len(a[0])):
    
#                for j in range(0,len (a)):
#                  if(i==j):
#                   if(min>a[i][j]):
#                    min=a[i][j]
#             print("cross min ",min)
                
#             min=a[0][1] 
#             for i in range(0,len(a[0])):
#                for j in range(0,len(a)):
#                  if(i+j==len(a)-1):  
#                     if(min>a[i][j]):
#                       min=a[i][j]
#             print("cross min ",min)
# b=demo()
# b.array()


# 4-> crosssum 

# class demo:
#     def array(self):
#                  a = [    
#                      [1, 2, 3],  
#                      [4, 5, 6],  
#                      [7, 8, 9]  
#                 ];  
#                  sum=0
#                  for i in range(0,len(a[0])):
#                    for j in range(0,len(a)):
#                         if(i==j ):
#                          sum=sum+a[i][j]
#                  print("cross sum= ",sum)
#                  sum=0
#                  for i in range(0,len(a[0])):
#                   for j in range(0,len(a)):
#                     if(i+j==len(a)-1):
#                      sum=sum+a[i][j]
#                  print("cross sum= ",sum)

# b=demo()
# b.array()

# rowandcolsmax
# class demo:
#     def array(self):
        
#         a = [    
#         [1, 2, 3],  
#         [4, 5, 6],  
#         [7, 8, 9]  
#          ];  

#         for i in range(0,len(a[0])):
#             max=a[i][0]
#             for j in range(0,len (a)):
#               if(max<a[i][j]):
#                  max=a[i][j]
#             print("Max element of rows ",max)
                   
 
#         for i in range(0,len(a[0])):
#             max=a[0][i]
#             for j in range(0,len (a)):
#               if(max<a[j][i]):
#                  max=a[j][i]
#             print("Max element of cols ",max)
  
# b=demo()
# b.array()                            

# rowandcolsmin
# class demo:
#     def array(self):
        
#         a = [    
#         [1, 2, 3],  
#         [4, 5, 6],  
#         [7, 8, 9]  
#          ];  

#         for i in range(0,len(a[0])):
#             min=a[i][0]
#             for j in range(0,len (a)):
#               if(min>a[i][j]):
#                  min=a[i][j]
#             print("Min element of rows ",min)
                   
 
#         for i in range(0,len(a[0])):
#             min=a[0][i]
#             for j in range(0,len (a)):
#               if(min>a[j][i]):
#                  min=a[j][i]
#             print("Min element of cols ",min)
  
# b=demo()
# b.array()
# rowandcolssum
# class demo:
#     def array(self):
        
#         a = [    
#            [1, 2, 3],  
#            [4, 5, 6],  
#            [7, 8, 9]  
#         ];  
#         rows=(len(a))     
#         cols=(len(a[0]))
       
#         for i in range(0,rows):
#           sumRow=0 
#           for j in range(0,cols):
#             sumRow = sumRow + a[i][j];  
#           print("Sum of " + str(i+1) +" row: " + str(sumRow))  


       
#         for i in range(0,rows):
#           sumcols=0 
#           for j in range(0,cols):
#            sumcols = sumcols + a[j][i];  
#           print("Sum of " + str(i+1) +" cols: " + str(sumcols))  

# b=demo()
# b.array()


    
# class Ascending :
#     def check(self) :
#         a = [
#             [9,8,7],
#             [1,2,4],
#             [3,2,1]
#         ]

#         for i in range(0,len(a[0])) :
#             for j in range(i+1,len(a)) :
#                 if (a[i] > a[j]) :
#                     temp = a[i]
#                     a[i] = a[j]
#                     a[j] = temp

#         print('Ascending order')

#         for i in range(0,len(a[0])) :
#             for j in range(0,len(a)) :
#                 print(a[i][j],end=' , ') 
#             print()
# obj = Ascending()  
# obj.check()   

# class Descending :
#     def check(self) :
#         a = [
#             [9,8,7],
#             [1,2,4],
#             [3,2,1]
#         ]

#         for i in range(0,len(a[0])) :
#             for j in range(i+1,len(a)) :
#                 if (a[i] < a[j]) :
#                     temp = a[i]
#                     a[i] = a[j]
#                     a[j] = temp

#         print('Descending order')

#         for i in range(0,len(a[0])) :
#             for j in range(0,len(a)) :
#                 print(a[i][j],end=' , ') 
#             print()

# obj = Descending()  
# obj.check()     

                           
                           

# class third_Array_saves :
#     def save_total(self) :
#         Arr1 = [
#             [1,2,3,4],
#             [5,6,7,8]
#         ]

#         Arr2 = [
#             [1,2,3,4],
#             [5,1,4,1]
#         ]

#         Arr3 = []

#         for i in range (0,len(Arr1)) :
#             row_sum = []
#             for j in range(0,len(Arr1[i])) :
#                 row_sum.append(Arr1[i][j] + Arr2[i][j])
#             Arr3.append(row_sum)

#         for i in range(0,len(Arr1)) :    
#             print(i,Arr3[i]) 
#         print()      

# obj = third_Array_saves() 
# obj.save_total()                             

class MyClass:
	pass
