#!/usr/bin/python
#
# Priority Queue implemented as a Heap.
# Heap implemented as array based complete binary tree.
# Given a node K in an array A:
#	A[ parent=K/2 | node K | left child=K*2 | right child=K*2+1 ]
#
# pages.cs.wisc.edu/~vernon/cs367/notes/11.PRIORITY-Q.html



class priority_queue():
	arr = []
	def __init__(self, a=[0]):
		self.arr = a
		pass

	def __eq__(self, x):
		return self.arr.__eq__(x)

	def empty(self):
		return (len(self.arr) == 1)

	def insert(self, val):
		self.arr.insert(len(self.arr), val)		# add to end of array
								
		k = len(self.arr)-1	# maintain descending order, swap if child > parent
		parent = k / 2
		while parent > 0 and self.arr[k] > self.arr[parent]:
			self.arr[k], self.arr[parent] = self.arr[parent], self.arr[k]
			k = parent
			parent = k / 2

	def popmax(self):
		if self.empty():
			return None

		val = self.arr[1]	# last element becomes new root and delete last
		self.arr[1] = self.arr[len(self.arr) - 1]
		self.arr.pop()

		# maintain ordering swapping with largest child until parent > child
		k = 1
		while k * 2 < len(self.arr):
			left = k * 2
			right = k * 2 + 1

			lval = self.arr[left]
			rval = self.arr[right] if right < len(self.arr) else 0

			if lval > rval and self.arr[k] < lval:
				self.arr[k], self.arr[left] = self.arr[left], self.arr[k]
				k = left
			elif self.arr[k] < rval:
				self.arr[k], self.arr[right] = self.arr[right], self.arr[k]
				k = right
			else:
				break

		return val

	def breadth_first(self):
		# return the list - BFS sequential ordering comes for free
		return self.arr


print 'Testing multiple insert'
ex1 = [ 0, 35, 26, 33, 15, 24, 5, 4, 12, 1, 23, 21, 2 ]
pq1 = priority_queue(ex1)
pq1.insert(34)
pq1.insert(6)
pq1.insert(40)
pq1.insert(28)
ex1_res = [ 0, 40, 28, 35, 26, 24, 33, 34, 15, 1, 23, 21, 2, 5, 4, 6, 12 ]
try:
	assert(pq1 == ex1_res)
except AssertionError:
	print 'expected', ex2_res
	print 'returned', pq2.arr

print 'Testing single remove'
ex2 = [ 0, 35, 26, 34, 15, 24, 33, 4, 12, 1, 23, 21, 2, 5 ]
pq2 = priority_queue(ex2)
pq2.popmax()
ex2_res = [ 0, 34, 26, 33, 15, 24, 5, 4, 12, 1, 23, 21, 2 ]
try:
	assert(pq2 == ex2_res)
except AssertionError:
	print 'expected ', ex2_res
	print 'returned ', pq2.arr


print 'Testing multiple removals'
ex3_res = [ 0, 24, 23, 5, 15, 21, 2, 4, 12, 1 ]
pq2.popmax()
pq2.popmax()
pq2.popmax()
try:
	assert(pq2 == ex3_res)
except AssertionError:
	print 'expected ', ex3_res
	print 'returned ', pq2.arr

print "Testing emptied queue"
while pq2.popmax():
	pass
try:
	assert(pq2 == [0])
except AssertionError:
	print 'expected ', [0]
	print 'returned ', pq2.arr

