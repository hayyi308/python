
num =  int(input('Please enter a number: '))

tmp = num
factor = []

mul_factor = 1    

while (num != mul_factor):
  for i in range(2, num/2):
    if  ((tmp % i) == 0):
      factor.append(i)
      tmp = tmp/i
      mul_factor = mul_factor*i
      #print  str(tmp)+', '+str(i)+', '+str(mul_factor)
      break    
  
    elif((len(factor) == 0) and (i == (num/2-1))): 
      factor.append(num) 
      print  str(num)+' is a prime.'
      mul_factor = num
      break  


def print_factor():
  for i in range(0, len(factor)):
    print  str(factor[i]),
    if  (i != (len(factor)-1)):
      print ' *',
  return
	
	
print  str(num)+' = ',
print_factor()


