
s = [ 'abc', 'def', 'Abc' ]
if "Abc" in s:
    print "match"
else:
    print "no match"

print s
t = s
t[0] = "foo"
print s
q = tuple(s)
# blow up as this is now immutable
q[0] = "bar"
print s