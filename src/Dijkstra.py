def dijkstra(net, s, t):
	# sanity check
	if s == t:
		return "The start and terminal nodes are the same. Minimum distance is 0."
	if not net.has_key(s):
		return "There is no start node called " + str(s) + "."
	if not net.has_key(t):
		return "There is no terminal node called " + str(t) + "."
	# create a labels dictionary
	labels={}
	# record whether a label was updated
	order={}
	# populate an initial labels dictionary
	for i in net.keys():
		if i == s: labels[i] = 0 # shortest distance form s to s is 0
		else: labels[i] = float("inf") # initial labels are infinity
	from copy import copy
	drop1 = copy(labels) # used for looping
	## begin algorithm
	while len(drop1) > 0:
		# find the key with the lowest label
		minNode = min(drop1, key = drop1.get) #minNode is the node with the smallest label
		print "minNode", minNode, drop1
		# update labels for nodes that are connected to minNode
		for i in net[minNode]:
			print "Checking ", minNode, i
			if labels[i] > (labels[minNode] + net[minNode][i]):
				print "here"
				labels[i] = labels[minNode] + net[minNode][i]
				drop1[i] = labels[minNode] + net[minNode][i]
				order[i] = minNode
				print "here", labels, drop1, order
		del drop1[minNode] # once a node has been visited, it's excluded from drop1
	## end algorithm
	# print shortest path
	temp = copy(t)
	rpath = []
	path = []
	while 1:
		rpath.append(temp)
		if order.has_key(temp): temp = order[temp]
		else: return "There is no path from " + str(s) + " to " + str(t) + "."
		if temp == s:
			rpath.append(temp)
			break
	print "Rpath", rpath
	for j in range(len(rpath)-1,-1,-1):
		path.append(rpath[j])

	print labels, order, drop1
	return "The shortest path from " + s + " to " + t + " is " + str(path) + ". Minimum distance is " + str(labels[t]) + "."


if __name__ == '__main__':
	net = {'0':{'1':100, '2':300},
	   '1':{'3':500, '4':500, '5':100},
	   '2':{'4':100, '5':100},
	   '3':{'5':20},
	   '4':{'5':20},
	   '5':{}
	   }
	print dijkstra(net, '2', '5')