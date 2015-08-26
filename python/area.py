#!/usr/bin/python

# area = 2 * pi * r^2

import math

r = 5
print "r = ", r
area = 2 * 3.14 * (r * r)
print "area = ", area

# with math lib
area = 2 * 3.14 * math.pow(r, 2)
print "area = ", area
