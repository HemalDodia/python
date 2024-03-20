import datetime as dt
a=dt.datetime.now()
print('data=',a)

# currentdate=a.date()
# print('data=',currentdate)\
    
# currenttime=a.time()
# print('data=',currenttime)   


# # 1->Python DateTime Format Using Strftime()

# convert to date String
# date = a.strftime("%d/%m/%Y")
# print('Date String:', date)

# time
# time = a.strftime("%H:%M:%S")
# print('Time String:', time)

# year
# year = a.strftime("%Y")
# print('Year String:', year)

# second fromat for year
# year = a.strftime("%y")
# print('Year String:', year)

# Month
# month = a.strftime("%m")
# print('Month String:', month)

# Day
# day = a.strftime("%d")
# print('Day String:', day)

# Returns the full name of the weekday
# weekday = a.strftime("%A")
# print('weekday String:', weekday)

# second fromat for weekday
# weekday  = a.strftime("%a")
# print('weekday String:', weekday)


#  Returns the full name of the month
# month  = a.strftime("%B")
# print('month String:', month)

# second fromat for month
# month  = a.strftime("%b")
# print('month String:', month)

# Returns the hour. from 01 to 23.
# hour = a.strftime("%H")
# print('hour String:', hour)

#  Returns the hour in 12-hours format.
# hour1 = a.strftime("%I")
# print('hours1 String:', hour1)

#  Returns the minute, from 00 to 59
# mintue  = a.strftime("%M")
# print('mintue String:', mintue)

#  Returns the second, from 00 to 59.
# second  = a.strftime("%S")
# print('second String:', second)

#  Return the microseconds from 000000 to 999999
# mircosecond  = a.strftime("%f")
# print('mircosecond String:', mircosecond)

#  Return time in AM/PM format
# AMandPM= a.strftime("%p")
# print('AMandPM String:', AMandPM)

# : Returns a locale’s appropriate date and time representation
local= a.strftime("%c")
print('local date and time String:', local)

#  Returns a locale’s appropriate date representation
# date= a.strftime("%x")
# print('date String:', date)

#  Returns a locale’s appropriate time representation
# time= a.strftime("%X")
# print('time String:', time)


#  Return the UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if 
# the object is naive).
# utc_offset= a.strftime("%z")
# print('utc_offset String:', utc_offset)
    
#  Return the Time zone name  
# timezone= a.strftime("%Z")
# print('timezone String:', timezone)

#  Returns the day of the year from 01 to 366  
# dayoff= a.strftime("%j")
# print('dayoff String:', dayoff)

# : Returns weekday as a decimal number, where 0 is Sunday and 6 is 
# Saturday
# print('Weekday Number:', int(weekday))


#  Returns the week number of the year (Sunday as the first day of the 
# week) from 00 to 53
# week= a.strftime("%U") 
# print('Week Number:', int(week))

# Returns the week number of the year (Monday as the first day of the 
# week) from 00 to 53
# week= a.strftime("%W") 
# print('Week Number:', int(week))

#  Use the %H-%M-%S format code to display time in 24-hours format
# a_time = dt.datetime.now()
# print('Current Time:', a_time)

# print("Time in 24 hours format:", a_time.strftime("%H-%M-%S"))
# print("Time in 12 hours format:", a_time.strftime("%I-%M-%S"))