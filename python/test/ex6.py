# Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13,...

fib_list = []

num = int(input('Please input number of Fibonacci: '))

def fib(n):
  for i in range(0, n):
    if  i == 0:
      fib_list.append(0)
    elif  (i == 1) or (i == 2):
      fib_list.append(1)
    else: 
      x = fib_list[i-1]+fib_list[i-2]
      fib_list.append(x)
      
  print fib_list
  return


fib(num)
