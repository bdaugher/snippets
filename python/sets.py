

odds = set(range(1,10,2))
evens = set(range(2,11,2))
toten = set()

print dir(odds)
print "odds: ", odds
print "evens: ", evens

toten.update(set().union(odds,evens))
print "toten: ", toten
