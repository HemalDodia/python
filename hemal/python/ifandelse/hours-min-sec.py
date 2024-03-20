hours = int(input('Enter Hours = '))
minute = int(input('Enter Minute = '))
second = int(input('Enter Second = '))

Finalsecond = second
global Minute, FinalMinute, FinalHour

if (Finalsecond > 60) : 
    Minute = Finalsecond  //  60
    Finalsecond %= 60
    print(f'{Minute} minutes and {Finalsecond} seconds')

    FinalMinute = minute + Minute
    FinalHour = hours + FinalMinute // 60
    print(f'{FinalHour} hours, {FinalMinute % 60} minutes, and {Finalsecond} seconds')     
     
else :
    print(f'{hours} hours, {minute %60} minute, and  {second} seconds')

# hours1 = int(input('Enter Hours 1 = '))
# hours2 = int(input('Enter Hours 2 = '))
# minute1 = int(input('Enter Minute 1 = '))
# minut2 = int(input('Enter Minute 2 = '))
# second1 = int(input('Enter Second 1 = '))
# second2 = int(input('Enter Second 2 = '))

# Finalsecond = second1 + second2 
# global Minute, FinalMinute, FinalHour

# if (Finalsecond > 60) : 
#     Minute = Finalsecond  //  60
#     Finalsecond %= 60
#     print(f'{Minute} minutes and {Finalsecond} seconds')

#     FinalMinute = minute1 + minut2 + Minute
#     FinalHour = hours1 + hours2 + FinalMinute // 60
#     print(f'{FinalHour} hours, {FinalMinute % 60} minutes, and {Finalsecond} seconds')     
     
# else :
#     print(f'{hours1} {hours2} hours, {minute1, minut2 %60} minute, and  {second1, second2} seconds')    