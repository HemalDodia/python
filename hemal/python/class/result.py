class student_result:
    def result(self):
        a=int(input("a=="))
        print(a) 
        b=int(input("b==="))
        print(b)
        c=int(input("c=="))
        print(c)
        d=int(input("d=="))
        print(d)
        sum=a+b+c+d
        print("sum=",sum)
        avg=sum/4
        print("avg=",avg)
        sum=a+b+c+d     
        per=sum*100/400
        print("per=",per)
        grade=per
        if grade>=91 and grade<=100:
         print("grade=A1") 
        elif grade>85 and grade<=90:
            print("grade=A2")
        elif grade>80 and grade<=85:
            print("grade=B1")
        elif grade>75 and grade<=80:
            print("grade=B2")
        elif grade>70 and grade<=75:
            print("grade=B")
        elif grade>=60 and grade<=70:
            print("grade=C") 
        elif grade>=50  and grade<60 :
            print("grade=D")
        elif grade>=40  and grade<49 :
            print("grade=E")
        elif grade>=33  and grade<39 :
            print("grade=F")
        else:
          print("fail")      
        
        if grade>=33:
         if a>b and a>c and a>d:
          print("a is max")                
         elif  b>c and b>d:
            print("b is max")
         elif c>d :
           print("c is max")    
        else:
          print(" d is max")
                      
        if a<b and a<c and a<d:
         print("a is min")                
        elif  b<c and b<d:
          print("b is min")
        elif c<d :
         print("c is min")    
        else:
          print(" d is min")

f=student_result()
f.result()

    