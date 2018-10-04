
import math

for i in range(100, 999):
  #print 'i = '+str(i)

  one = i % 10
  ten = ((i-one)/10) % 10
  hundred = ((i-ten*10-one)/100) % 10
  
  #print str(hundred)+', '+str(ten)+', '+str(one)
  lily = math.pow(hundred, 3) + math.pow(ten, 3) + math.pow(one, 3)
  if  i == lily:
    print  str(i)


