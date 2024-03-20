# cap = small = digit = spec = 0
# user = [None]
# i = 0
# user = input('Enter password = ') 

# while (i<len(user)) :
#     if (user[i]>='A' and user[i]<='Z') :
#         cap = 1

#     elif (user[i]>='a' and user[i]<='z') :
#         small += 1

#     elif (user[i]>='0' and user[i]<='9') :
#         digit = 1

#     else :
#         spec = 1
#     i+=1       

# if (cap and small and digit and spec == 1) :
#     print('password is right')
# else :
#     print('wrong password try agian password')  


# 8 digit number password check  program
 
# l, u, p, d = 0, 0, 0, 0
# s = "Hemal_@"
# if (len(s) >= 8):
#     for i in s:
 
#         # counting lowercase alphabets 
#         if (i.islower()):
#             l+=1           
 
#         # counting uppercase alphabets
#         if (i.isupper()):
#             u+=1           
 
#         # counting digits
#         if (i.isdigit()):
#             d+=1           
 
#         # counting the mentioned special characters
#         if(i=='@'or i=='$' or i=='_'):
#             p+=1          
# if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(s)):
#     print("Valid Password")
# else:
#     print("Invalid Password")