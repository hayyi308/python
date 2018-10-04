singer = {}

for i in range(0, 5):
  name = raw_input('singer name: ')
  score = int(input('singer score: '))
  singer[name] = score

print singer

for i in range(0, 5):
  search_name = raw_input('Search the singer Name: ')
  print(singer.get(search_name, 'Cannot find the name!')) 
  
