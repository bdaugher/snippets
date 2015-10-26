#!/usr/bin/python
#
# Q: Determine if a string has all unique characters.
# A: Iterate over string using hash or array[26] to count letter frequency
#
# Q: What if you cannot use additional data structures?
# A: Sort, update in place (destructively), e.g. abba => a2b2

tests = {
	0: 'all good men',
	1: 'anteaters and lions on the serengheti',
	2: 'beyond a shadow of a doubt',
}

print tests.viewvalues()
print tests.viewkeys()


