# 1, 1, 1', 1', 1', 1', 1', 1',
#       1 , 1 , 1', 1', 1', 1', 
#           1 , 1 , 1', 1', 1',
#               2 , 2 , 2', 2', 
#                   3 , 3 , 3',
#                       5 , 5 , 
#                           8
#----------------------------------
# 1, 1, 2,  3,  5,  8,  13, 21,....

# Fibonacci sequence 

rabbit_num = []

for i in range(0, 12):
  if (i == 0) or (i == 1):
    rabbit_num.append(1)
  else:
    num = rabbit_num[i-1] + rabbit_num[i-2]
    rabbit_num.append(num)

print rabbit_num

