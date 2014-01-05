from copy import copy

def dijkstra(network, startNode, endNode):
	minimumCost = {}

	for node in network.keys():
		if node == startNode:
			minimumCost[node] = 0
		else:
			minimumCost[node] = float("inf")

	stillToVisit = copy(minimumCost)
	order = {}
	
	while stillToVisit:
		minNode = min(stillToVisit, key = stillToVisit.get)
		for connectedNode in network[minNode]:
			if minimumCost[connectedNode] > (minimumCost[minNode] + network[minNode][connectedNode]):
				minimumCost[connectedNode] = minimumCost[minNode] + network[minNode][connectedNode]
				stillToVisit[connectedNode] = minimumCost[minNode] + network[minNode][connectedNode]
				order[connectedNode] = minNode
		del stillToVisit[minNode]

	path = [endNode]
	nextNode = endNode
	while True:
		if order[nextNode] == startNode:
			path = [order[nextNode]] + path
			break
		if order[nextNode] in order:
			path = [order[nextNode]] + path
			nextNode = order[nextNode]
		else:
			return "There is no path from", startNode, "to", endNode

	return "The shortest path from", startNode, "to", endNode, "is", path, "cost", minimumCost[endNode]

if __name__ == '__main__':

	net = {'0':{'1':100, '2':300, '5':500},
	   '1':{'3':500, '4':500, '5':100},
	   '2':{'4':100, '5':100},
	   '3':{'5':20},
	   '4':{'5':20},
	   '5':{}
	   }
	print dijkstra(net, '0', '5')