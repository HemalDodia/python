# class Check_pali :
#     def set(self) :
#         Num = int(input('Enter Any Number = '))
#         return Num

#     def get(self,v) :

#         Real_val = v  
#         total = 0

#         while (v > 0) :    
#             rem = v %10
#             total = total *10 +rem
#             v = v//10
            
#         if (total == Real_val) :
#             print('Its Pali Number')

#         else :
#             print('Its Not Pali Number')       

# obj = Check_pali()

# v = obj.set()   
# obj.get(v)

# # 2-> arm strong number 

class Check_pali :
    def set(self) :
        Num = int(input('Enter Any Number = '))
        return Num

    def get(self,v) :

        Real_val = v  
        total = 0

        while (v > 0) :    
            rem = v %10
            total = total + rem * rem *rem
            v = v//10
            
        if (total == Real_val) :
            print('Its Armstrong Number')

        else :
            print('Its Not Armstrong Number')       

obj = Check_pali()

v = obj.set()   
obj.get(v)