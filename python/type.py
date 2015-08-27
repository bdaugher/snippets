 
a = list('abcdefghijklmnopqrstuvwxyz')
b = set([1, 3, 5, 7, 9])
c = frozenset(['a', 'b', 'c'])
d = dict({'a' : 1, 'b' : 2, 'c' : 3})
e = str('abc')



    
reg1 = (1 << 2) | (1 << 7) | (1 << 24)   # IRQs on 2nd, 7th, 24th bits
mask = 0x000000FF
reg1 &= mask
print reg1, mask
if reg1 & (1 << 2):
    print 'second bit is set'
if reg1 & (1 << 3):
    print 'third bit is set'