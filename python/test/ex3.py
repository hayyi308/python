
#  x+100 = n^2, x+100+168 = m^2
#  m^2-n^2 = (m+n)*(m-n) = 168 
#  let  (m+n)=i, (m-n)=j
#  => i*j = 168
#  => (i+j)/2 = m,  (i-j)/2 = n
#  ==> i & j is even, i>=2, j>=2
#  ==> 1 < i < 168/2+1


for i in range(1, 85):
  if  168 % i == 0:
    j = 168/i
    if  (i > j) and ((i+j)%2 == 0) and ((i-j)%2 == 0):
      m = (i+j)/2
      n = (i-j)/2
      x = n*n - 100
      print 'x = '+str(x)

