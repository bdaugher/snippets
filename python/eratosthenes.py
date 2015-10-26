#!/usr/bin/python
#
# Find prime numbers using 'sieve of Eratosthenes'
# First elimnate all even values starting with n=2, second, iterate
# over n = n + 1 elimating values n is a divisor for
#


rangemax = 1024

primes = range(1, rangemax + 1)

print 'input', primes

for v in primes[2:]:			# start at two
	if v % 2 == 0:			# eliminate evens
		print 'eliminating', v
		primes.remove(v)

for v in primes[2:]:			# eliminate factors of the divisor
	if v in primes:			# guard against list removals
		for v2 in primes[primes.index(v)+1:]:
			if v2 % v == 0:
				print 'eliminating', v2
				primes.remove(v2)

print 'primes', primes

