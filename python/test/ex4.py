# How to know the leap year?
# year % 4 != 0  => not the leap year
# year % 4 == 0 and year % 100 != 0   => the leap year
# year % 100 == 0 and year % 400 != 0  => not the leap year
# year % 400 == 0  => the leap year

import sys

M = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

year = int(raw_input('year = '))
month = int(raw_input('month = '))
if  (month == 0) or (month > 12):
  sys.exit('month error')
date = int(raw_input('date = '))
if  date > M[month-1]:
  sys.exit('date error')

days = 0
for i in range(0, month-1):
  days += M[i]
days += date

# Is the leap year or not?
if  month > 2:
  if  year % 4 != 0:
    print 'not the leap year~'
  elif  (year%4 == 0) and (year%100 != 0):
    days+=1 
  elif  (year%100 == 0) and (year%400 != 0):
    print 'not the leap year~'
  elif  (year%400 == 0):
    days+=1

print 'days = '+str(days)


