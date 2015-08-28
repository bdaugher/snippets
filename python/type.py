 
a = list('abcdefghijklmnopqrstuvwxyz')
b = set([1, 3, 5, 7, 9])
c = frozenset(['a', 'b', 'c'])
d = {'a' : 1, 'b' : 2, 'c' : 3}
d2 = dict()
e = str('abc')


print "dictionary population using list comprehension"
d3 = dict(zip(range(0,10), range(100,110)))
print d3
d4 = dict(zip(range(0,10), [c for c in a]))
print d4
d5 = {v : a[v] for v in range(len(a))}
print d5
d6 = {k : v for k, v in enumerate(a)}
print d6
print d6.keys()
print d6.values()

print "bit masking"
reg1 = (1 << 2) | (1 << 7) | (1 << 24)   # IRQs on 2nd, 7th, 24th bits
mask = 0x000000FF
reg1 &= mask
print reg1, mask
if reg1 & (1 << 2):
    print 'second bit is set'
if reg1 & (1 << 3):
    print 'third bit is set'
    
# given two lists count the word frequency
print "word frequency"
list1 = ['abc', 'def', 'ghi', 'jkl', 'abc', 'ghi']
list2 = ['ghi', 'jkl', 'mno', 'pqr', 'jkl']
freq = {}
for word in list1 + list2:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1
print freq
words1 = {k : v for k, v in enumerate(list1)}
words2 = {k : v for k, v in enumerate(list2)}
