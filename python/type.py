 
a = list('abcdefghijklmnopqrstuvwxyz')
b = set([1, 3, 5, 7, 9])
c = frozenset(['a', 'b', 'c'])
d = dict({'a' : 1, 'b' : 2, 'c' : 3})
e = str('abc')





bits = 1
print "bits:", bits, " bits << 1:", bits << 1
if (1 << 1) & 0x2:
    print "2nd bit set"