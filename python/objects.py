#!/usr/bin/python

def localscope(x):
	print 'locals localscopt(): ', locals()
	print 'x = x + 1: ', id(x), type(x), x

	x = x + 1
	y = x
	z = y
	print 'y = x: ', id(y), type(y), y
	print 'z = y: ', id(z), type(z), z

	y = y + 1
	print 'y = x: ', id(y), type(y), y
	print 'z = y: ', id(z), type(z), z

	z = z + 3
	print 'z = y: ', id(z), type(z), z

	print 'returning z: ', id(z), type(z), z

	print 'returning from localscope() locals: ', locals()
	return z

print '__main__ locals: ', locals()

a = 5
print 'pre call  a: ', id(a), type(a), a
a = localscope(a)
print 'post call a: ', id(a), type(a), a

print '__main__ locals: ', locals()

