#!/usr/bin/python
# flip only 1 bit from 0 to 1. What is the longest sequence of 1's possible?

import sys

# test input
tests = (205, 211, 235, 247)

def ones_sequence(bits):
	sequence_cnt = 0
	longest_sequence = 0
	flipped_sz = 0
	i = 0
	sz = sys.getsizeof(bits)

	# start at LSB, test each bit for 1, have one chance to flip bit
	# break the loop when it doesn't match
	# start by testing for one
	while i < sz:
		if (bits & 1 << i):
			sequence_cnt = sequence_cnt + 1
			if (sequence_cnt > longest_sequence):
				longest_sequence = sequence_cnt
		elif flipped_sz == 0:
			# see if i + 1 == 1, if so we can continue
			pass
		else:
			sequence_cnt = 0
			
		i = i + 1

	return longest_sequence


longest_sequence = 0
longest = 0

for bits in tests:
	print bin(bits)
	seq_cnt = ones_sequence(bits)
	if seq_cnt > longest_sequence:
		longest_sequence = seq_cnt
		longest = bits

print bin(longest), ' has the longest contiguous sequence', longest_sequence


