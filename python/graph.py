#!/usr/bin/python
#
# implement a graph using a dictionary of lists
#

graph = {
	'1' : ['2', '3'], 
	'2' : ['1'],
	'3' : ['1'],
}

print type(graph), id(graph)
print dir(graph)
print graph

print graph.keys()
print graph.viewkeys()
print graph.values()
print graph.viewvalues()
print graph.items()

# pre-order
def preorder_graph(g):
	# print, left, right
	return

# post-order (depth first search)
def postorder_graph(g):
	# left, right, print
	return

# in-order (depth first search)
def inorder_graph(g):
	# left, print, right
	return



