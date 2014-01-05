import time, random

def quickSort(theList):
	if len(theList) > 1:
		lesser, greater = [], []
		for x in theList[1:]:
			if x <= theList[0]:
				lesser.append(x)
			else:
				greater.append(x)
		return quickSort(lesser) + [theList[0]] + quickSort(greater)
	else:
		return theList

population = 400000

myList = random.sample(xrange(population), population)
start_time = time.time()
result = quickSort(myList)
finish_time = time.time()
print "executed in", finish_time - start_time, "seconds"
print "Correct: ", result == sorted(myList)