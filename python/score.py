score = [10, 30, 50, 70, 90]

print "score: "
for num in range(0, len(score)):
    print str(score[num])+" ",

print "\naverage: "+str(sum(score)/len(score))

print "new score: "
for num in range(0, len(score)):
    score[num] = score[num]**0.5*10 
    print str(score[num])+" ",

print "\nnew average: "+str(sum(score)/len(score))
