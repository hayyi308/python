# How to verify that the number is a prime? 
# Ans. if (number % x) == 0, 2 < x < x^0.5

import math

def prime(num):
  if(num < 1):
    return 0
  else:
    for x in range(2, int(math.sqrt(num)+1)):
      if  (num % x) == 0:
        #print 'x = '+str(x)
        return 0
    return 1

count = 0    
print  'Show prime between 101~200:'  
for i in range(101, 200):
  #print 'i = '+str(i)
  if prime(i) == 1:
    print  str(i)
    count+=1

print 'total prime = '+str(count)    
