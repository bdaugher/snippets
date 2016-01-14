

odds = set(range(1,10,2))
evens = set(range(2,11,2))
toten = set()

print dir(odds)
print "odds: ", odds
print "evens: ", evens

# union
toten |= odds | evens
print "toten: ", toten

# intersection
twopower = set([2**x for x in range(10)])
print twopower
overlap = odds & twopower
print "intersection of odds and powers of two: ", overlap
overlap = evens & twopower
print "intersection of evens and powers of two: ", overlap

# exclusive
print "difference of evens and powers of two: ", evens.difference(twopower)

# create immutable shallow copy & update original
scopy = frozenset(evens.copy())
evens.remove(10)
print "evens without ten", evens
print "shallow immutable copy of evens: ", scopy
scopy.remove(2)
print "shallow immutable copy of evens: ", scopy
