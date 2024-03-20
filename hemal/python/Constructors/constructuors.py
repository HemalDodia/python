# class demo:
#     # default constructor
# 	def __init__(self):
# 		self.demo1 = "my name is hemal"
# 	def print_Geek(self):
# 		print(self.demo1)
# obj = demo()
# obj.print_Geek()


# 1-> asc and dsc order
class demo:
    list=[12,34,54,67,89]
    def __init__(self,a): 
        self.list=a
        for i in range(0,len(self.a)):
                print('self.a',i,'=',self.a[i])
                for i in range(0,len(self.a)):  
                 for j in range(i+1,len(self.a)):
                    if(self.a[i]>self.a[j]) :
                        temp=self.a[i]
                        self.a[i]=self.a[j] 
                        self.a[j]=temp  
        print('self.asc order print')
    def array1(self):    
        for i in range(0,len(self.a)):
                print(a[i])
                for i in range(0,len(self.a)):
                 for j in range(i+1,len(self.a)):
                     if(self.a[i]<self.a[j]) :
                        temp=self.a[i]
                        self.a[i]=self.a[j] 
                        self.a[j]=temp  
        print('dsc order print')
    def print_Geek(self):
         for i in range(0,len(self.a)):
              print(self.a[i])
obj = demo()
obj.print_Geek()
