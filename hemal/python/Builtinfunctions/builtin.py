# 1 =abs function
# x = abs(3+5j)
# print(x) 


# 2= min and max function
# a=[1,5,3,9]
# b=[1,4,6,3,7]
# print(max(a))
# print(min(a))

#  3= bin() Function
# print(bin(10))

#  4= bool() Function
# x = 10
# y = 10
# print(bool(x == y))
# z = 'Creative Design'
# print(bool(z))

# 5 =sum() Function
# s=sum([1,2])
# print(s)
# s = sum([1, 2, 2], 10)
# print(s) 
# s = sum([1 + 2j, 3 + 4j])
# print(s)
# s = sum([1 + 2j, 3 + 4j], 2 + 2j)
# print(s)
# s = sum([1 + 2j, 2, 1.5 - 2j])
# print(s) 

# 6=  float() Function
# print(float(8))
# print(float(7.19)) 
# print(float("-24.17")) 

# 7= format() Function
# print(format(123, "d"))
# # float arguments
# print(format(123, "f"))
# # binary format
# print(format(12, "b")) 



#  Left aligns the result (within the available space)
# a=123
# print(format(a,'<'))

#  Right aligns the result (within the available space)
# a=123
# print(format(a,'>'))

#  Center aligns the result (within the available space)
# a=123
# print(format(a,"^"))

#  Places the sign to the left most position
# a=123
# b=123
# print(format(a,"="))

#  Use a plus sign to indicate if the result is positive or negative
# a=123
# print(format(a,"+"))

# #  Use a minus sign for negative values only
# a=123
# print(format(a,"-"))

#  Use a leading space for positive number
# a=123
# # print(format(a,' '))

# Use a comma as a thousand separator
# a=123
# b=123
# print(format(a,','))

# #  Use a underscore as a thousand separator
# a=123
# print(format(a,'_'))

#  Binary format
# print(format(123, "b"))

#  Converts the value into the corresponding unicode character
 # print(format(123, "c"))
 
#  Decimal format
# print(format(123, "d"))

#  Scientific format, with a lower case e
# print(format(123, "e")

# Scientific format, with an upper case E
# print(format(123, "E")

# Fix point number format
# print(format(123, "f"), fixpoint number)

#   Fix point number format, upper case
# print(format(123, "F"), fixpoint number)

# General format
# print(format(123, "g")

#  General format (using a upper case E for scientific notations)
# print(format(123, "G")

#   Octal format
# print(format(123, "o")

# Hex format, lower case
# a=123
# print(format(a,'x'))

#  Hex format, upper case
# a=123
# print(format(a,'x'))

#  Number format
# a=123
# print(format(a,'n'))

#  Percentage format
# a=123
# print(format(a,'%'))


# 8= pow() Function
# # positive x, positive y (x**y) 
# print(pow(4, 2)) 

# # negative x, positive y 
# print(pow(-4, 2)) 


# with three prameter
# x = 4
# y = 7
# z = 3
# print(pow(x, y, z)) 


# 9. Python eval() Function
# a=2+3-4+(5*6)
# print(a)

# 10.Python slice() Function
#  Python slice() function example 
# Calling function 
# str1 = "Creative Multimedia"
# slic = slice(0,15,3) # returns slice object 
# slic2 = slice(-1,0,-3) # returns slice object 
# # We can use this slice object to get elements 
# str2 = str1[slic] 
# str3 = str1[slic2] # returns elements in reverse order 
# # Displaying result 
# print(str2) 
# print(str3)

# 11. divmod( ) function
# x=divmod(10, 3)
# print(x)

# 12. ORD( ) function
# x = ord("h")
# print(x)

# 13. Round() function

x = round(91.9)
print(x)
    
# 14.sorted() function
# sorted(iterable,key,reverse)
# t = (3,6,8,2,5,8,10)
# print(sorted(t,))

# 15. bool() in Python
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)
# x = bool(1)
# print(x)
# y = bool()
# print(y)