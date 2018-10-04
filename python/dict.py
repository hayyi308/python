dict = {}

for i in range(0, 5):
  key = raw_input('Input a string: ')
  value = int(input('Input a number: '))
  dict[key] = value  #add a key-value pair
  #del dict[key] => delete the specific key-value pair

print dict
