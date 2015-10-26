#!/usr/bin/python
#
# Merge Sort of: 9, 4, 7, 2, 3
#   split 1: 9, 4, 7                   split 2: 2, 3
#   split 3: 9, split 4: 4, 7          split 5: 2 split 6: 3
#               split 7: 4 split 8: 7
#
# Merge the two arrays, picking lowest value from either split
#	9 (5)	4 (3)
#	7 (4)	2 (1)
#	3 (2)
#


# pick the next lowest value from either a1 or a2 and insert it into a new list
def merge_halves(lower, upper):

	i = 0
	j = 0
	k = 0

	merged = []

	while j < len(lower) and k < len(upper):
		if lower[j] < upper[k]:
			merged.insert(i, lower[j])
			j = j + 1
		else:
			merged.insert(i, upper[k])
			k = k + 1
		i = i + 1

	while j < len(lower):
		merged.insert(i, lower[j])
		j = j + 1
		i = i + 1

	while k < len(upper):
		merged.insert(i, upper[k])
		k = k + 1
		i = i + 1

	return merged

def merge_sort(unsorted):

	if len(unsorted) <= 1:		# base case - nothing to sort
		return unsorted

	lower_half = merge_sort(unsorted[:len(unsorted) / 2])
	upper_half = merge_sort(unsorted[len(unsorted) / 2:])

	merged = merge_halves(lower_half, upper_half)

	return merged


t1 = range(1,111111111) # reverse sorted
t1.reverse()
t1_sorted = t1[:] # shallow copy
t1_sorted.sort()
t1 = merge_sort(t1)
if t1 == t1_sorted:
	print "success"
else:
	print "sort failed"


t2 = [0, 9, 5, 6, 8, 12, 3, 55]
t2_sorted = t2[:] # shallow copy
t2_sorted.sort()
t2 = merge_sort(t2)
if t2 == t2_sorted:
	print "success"
else:
	print "sort failed"



