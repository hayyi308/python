
score = int(input('Please enter the score: '))

if  (score >= 90):
  grade = 'A'
elif  (score >= 60):
  grade = 'B'
else:  
  grade = 'C'

print  'This score is '+grade+'-grade.'
