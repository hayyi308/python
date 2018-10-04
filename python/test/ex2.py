
print  'Please enter the profit of this month.'
profit = long(input('profit = '))

#rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
limit = [1000000, 600000, 400000, 200000, 100000, 0]

bonus = 0

for i in range(0, 6):
  if  profit > limit[i]:
    bonus += (profit - limit[i])*rate[i] 
    profit = limit[i] 


print  'bonus = '+str(bonus)



