#  if __name__ == '__main__': 
# => When *.py run directly, these codes will run.
# => Otherwise, these codes won't execute while *.py as a module. 

# strftime():  return a string about current time. 
# *.date.today(): get today
# *.timedelta(days=x): get x days
# ex.  *.date.today() + *.timedelta(days=1) => tomorrow
#      *.date.today() - *.timedelta(days=3) => the day before 3 days


import datetime

if __name__ == '__main__':
 
  # show the date of today.  dd/mm/yyyy 
  print(datetime.date.today().strftime('%d/%m/%Y'))
     
  # create the object of date
  shuminBirthDate = datetime.date(1988, 7, 22)
  print(shuminBirthDate.strftime('%d/%m/%Y'))
       
  # calculate the date
  shuminBirthNextDay = shuminBirthDate + datetime.timedelta(days=1) 
  print(shuminBirthNextDay.strftime('%d/%m/%Y'))
       
  # replace date   
  shuminFirstBirthday = shuminBirthDate.replace(year=shuminBirthDate.year + 1) 
  print(shuminFirstBirthday.strftime('%d/%m/%Y'))


