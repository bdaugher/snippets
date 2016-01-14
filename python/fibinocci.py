#!/usr/bin/python
# Fibonacci sequence
#   F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1
#       0, 1, 1, 2, 3, 5, 8, 13, 21, 24, 55, 89, 144

# example of swap in place 
x, y = 66, 22
print 'pre in place swap', x, y
x, y = y, x     # RHS is evaluated as tuple (y, x), then assignment into LHS
print 'post in place swap', x, y

# imperative solution
f = []
a, b = 0, 1
for i in range(10):
    a, b = b, a + b     # 2, 3 = (3, 2+3) >>> 3, 5
    f.append(a)
print f

# generator method
def fib():
    n, n2 = 0, 1
    while True:
        n, n2 = n2, n + n2 # RHS is tuple, evaluated, then LHS assignment
        yield n

f = fib()
seq = [ f.next() for x in range(10) ]
print seq

