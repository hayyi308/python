print "Show 9X9: "

for  i in range(1, 10):
  for j in range(1, 10): 
    print str(i)+"X"+str(j)+"=",

    mul = i*j
    if(len(str(mul)) == 1):
      print " "+str(mul),
    else:
      print str(mul),
    
    print str(" "),

    if(j==9):
      print "\n"

 


