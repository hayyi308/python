count = 0

for i in range(1, 5):
  for j in range(1, 5):
    if  j == i:
      continue
    else:
      for k in range(1, 5):
        if  (k==i) or (k==j):
          continue
        else:
          count = count+1
          print  str(i)+str(j)+str(k)

print  'count = '+str(count)
