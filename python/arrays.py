
evens = range(2, 12, 2)

for i in evens:
    print i,
print
    
# reverse list order
evens = evens[::-1]
    
for i in evens:
    print i,
print
    
if 7 in evens:
    print "there is an odd in even range"
else:
    print "seven is not in the even range"
    
if 6 in evens:
    print "six is in the even range"

half = len(evens) / 2
print "# evens: ", len(evens), " half slice: ", half
h1_evens = evens[len(evens)/2:]
h2_evens = evens[:len(evens)/2]
print "1st half evens: ", h1_evens, " 2nd half evens: ", h2_evens

