# a=[12,34,54,67,89]
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


class third_Array_saves :
    def save_total(self) :
        Arr1 = [
            [1,2,3,4],
            [5,6,7,8]
        ]

        Arr2 = [
            [1,2,3,4],
            [5,1,4,1]
        ]

        Arr3 = []

        for i in range (0,len(Arr1)) :
            row_sum = []
            for j in range(0,len(Arr1[i])) :
                row_sum.append(Arr1[i][j] + Arr2[i][j])
            Arr3.append(row_sum)

        for i in range(0,len(Arr1)) :    
            print(i,Arr3[i]) 
        print()      

obj = third_Array_saves() 
obj.save_total()  