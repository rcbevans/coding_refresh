class FlowerGarden:
	def __init__(self):
		pass
	
	'''
	def __init__(self, height, bloom, wilt):
		self.noFlowers = len(height)
		self.height = height
		self.bloom = bloom
		self.wilt = wilt
	'''
	
	def getOrdering(self, height, bloom, wilt):
		# Setup
		self.noFlowers = len(height)
		self.height = height
		self.remainingHeights = height[:]
		self.bloom = bloom
		self.wilt = wilt
		self.finalPositions = []
		self.flowerPlaced = [False] * self.noFlowers
		bestFlower = 0
		currentFlower = 0
		#
		'''
		for resultPosition in range(self.noFlowers):
			bestFlower = 0
			comparisonFlower = 0
			done = False
			while not done:
				while bestFlower < self.noFlowers and self.flowerPlaced[bestFlower]:
					bestFlower += 1
				comparisonFlower = bestFlower + 1
				while comparisonFlower < self.noFlowers and self.flowerPlaced[comparisonFlower]:
					comparisonFlower += 1
				#-----------------------------------------------------------------
				print "Position", resultPosition, "comparing best flower", bestFlower, "comparison flower", comparisonFlower
				if bestFlower < self.noFlowers and comparisonFlower < self.noFlowers:
					print "here 1"
					if self.flowersBlock(bestFlower, comparisonFlower):
						if self.height[comparisonFlower] < self.height[bestFlower]:
							bestFlower = comparisonFlower
						print "here 2"
						comparisonFlower += 1
					else:
						if self.height[comparisonFlower] > self.height[bestFlower]:
							bestFlower = comparisonFlower
						print "here3"
						comparisonFlower += 1
				else:
					print "here 4"
					self.finalPositions[resultPosition] = self.height[bestFlower]
					self.flowerPlaced[bestFlower] = True
					done = True
		return self.finalPositions
		'''

		print self.height

		#New method -> overlap table? Dynamic?
		self.Overlap = [[] for x in range(self.noFlowers)]
		done = False
		while not done:
			for i in range(self.noFlowers):
				for j in range(i+1, self.noFlowers):
					print "Comparing", i, j
					if self.flowersBlock(i, j):
						self.Overlap[i].append(j)
						if self.remainingHeights and self.height[i] in self.remainingHeights and self.height[j] == max(self.remainingHeights):
							print "I'm here", i, self.height[i], j, self.height[j]
							self.finalPositions.append(self.height[i])
							print self.remainingHeights, self.height
							self.remainingHeights.remove(self.height[i])
							self.flowerPlaced[i] = True
				if not self.Overlap[i] and self.remainingHeights and self.height[i] == max(self.remainingHeights):
					self.finalPositions.append(self.height[i])		
					self.remainingHeights.remove(self.height[i])
					self.flowerPlaced[i] = True
				if not self.remainingHeights:
					done = True
				print self.Overlap
				print self.finalPositions
				raw_input()
		print self.Overlap
		print self.remainingHeights
		return self.finalPositions

	def flowersBlock(self, flowerOne, flowerTwo):
		if self.bloom[flowerOne] < self.bloom[flowerTwo] and self.wilt[flowerOne] < self.bloom[flowerTwo]:
			return False
		elif self.bloom[flowerTwo] < self.bloom[flowerOne] and self.wilt[flowerTwo] < self.bloom[flowerOne]:
			return False
		else:
			print "Flowers block", flowerOne, flowerTwo
			return True

if __name__ == '__main__':

	
	## Test the flowersBlock function
	'''
	height = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
	bloom = [1, 3, 3, 1, 1, 2, 2, 1, 1, 3]
	wilt = [2, 4, 4, 2, 3, 4, 4, 3, 9, 6]
	
	height = [1,2,3,4,5,6]
	bloom = [1,3,1,3,1,3]
	wilt = [2,4,2,4,2,4]

	test = FlowerGarden(height, bloom, wilt)

	print test.flowersBlock(0, 1)
	print test.flowersBlock(2, 3)
	print test.flowersBlock(4, 5)
	print test.flowersBlock(0, 2)
	print test.flowersBlock(1, 3)
	##-------------------------------------------
	'''
	test = FlowerGarden()
	
	'''
	height = [3,2,5,4]
	bloom = [1,2,11,10]
	wilt = [4,3,12,13]
	# Returns: { 4,  5,  2,  3 }

	height = [1,2,3,4,5,6]
	bloom = [1,3,1,3,1,3]
	wilt = [2,4,2,4,2,4]
	# Returns: { 2,  4,  6,  1,  3,  5 }
	
	height = [5,4,3,2,1]
	bloom = [1,5,10,15,20]
	wilt = [5,10,14,20,25]
	#Returns: { 3,  4,  5,  1,  2 }
	'''

	height = [355, 432, 141, 84, 544, 650, 777, 499, 709, 764]
	bloom = [251, 18, 324, 87, 145, 118, 152, 52, 171, 160]
	wilt = [293, 200, 344, 234, 197, 281, 275, 342, 261, 262]
	#Returns: {355, 141, 84, 432, 499, 544, 650, 709, 764, 777}
	
	'''
	height = [1,2,3,4,5,6]
	bloom = [1,3,1,3,1,3]
	wilt = [2,4,2,4,2,4]
	#Returns {2, 4, 6, 1, 3, 5}
	'''

	print test.getOrdering(height, bloom, wilt)
	