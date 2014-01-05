import random, time

def MergeSort(theList):
	if len(theList) > 1:
		splitIndex = ((len(theList) + 1)/2)
		leftList = theList[0:splitIndex:1]
		rightList = theList[splitIndex:len(theList):1]
		return Merge(MergeSort(leftList), MergeSort(rightList))
	else:
		return theList

def Merge(leftList, rightList):
	result = []
	leftIndex, rightIndex = 0,0
	while leftIndex <= len(leftList) and rightIndex <= len(rightList):
		if leftIndex == len(leftList) and rightIndex == len(rightList):
			break
		elif leftIndex == len(leftList):
			result.append(rightList[rightIndex])
			rightIndex +=1
		elif rightIndex == len(rightList):
			result.append(leftList[leftIndex])
			leftIndex += 1
		elif leftList[leftIndex] <= rightList[rightIndex]:
			result.append(leftList[leftIndex])
			leftIndex += 1
		else:
			result.append(rightList[rightIndex])
			rightIndex += 1
	return result

population = 400000

listToSort = random.sample(xrange(population), population)
start_time = time.time()
result = MergeSort(listToSort)
stop_time = time.time()
print "executed in", stop_time - start_time, "seconds"
print "Correct:", result == sorted(listToSort)