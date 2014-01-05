class FlowerGarden:

  def getOrdering(self, height, bloom, wilt):
    self.height = height
    self.bloom = bloom
    self.wilt = wilt

    noPlants = len(height)
    correctPositions = [-1] * noPlants
    plantPlaced = [False] * noPlants
    print self.height

    for resultPosition in range(0, noPlants):
      bestPlant = 0
      comparisonPlant = 0
      done = False
      while not done:
        if plantPlaced[comparisonPlant]:
          while comparisonPlant < noPlants and plantPlaced[comparisonPlant]:
            comparisonPlant += 1
        if plantPlaced[bestPlant]:
          while bestPlant < noPlants and plantPlaced[bestPlant]:
            bestPlant += 1
        if bestPlant >= comparisonPlant:
          comparisonPlant = bestPlant + 1
        if bestPlant < noPlants and comparisonPlant < noPlants:
          if self.plantsOverLap(bestPlant, comparisonPlant) and not plantPlaced[comparisonPlant]:
            if height[bestPlant] > height[comparisonPlant]:
              bestPlant = comparisonPlant
            comparisonPlant += 1
            while comparisonPlant < noPlants and plantPlaced[comparisonPlant]:
              comparisonPlant += 1
          else:
            if height[comparisonPlant] > height[bestPlant] or plantPlaced[bestPlant]:
              bestPlant = comparisonPlant
            comparisonPlant += 1
        if comparisonPlant >= noPlants:
          print bestPlant
          done = True
          plantPlaced[bestPlant] = True
          print plantPlaced
      
      correctPositions[resultPosition] = height[bestPlant]
      print correctPositions

    return correctPositions

  def plantsOverLap(self, plant1, plant2):
    if (self.bloom[plant1] <= self.wilt[plant2] and self.bloom[plant2] <= self.wilt[plant1]):
      return True
    elif (self.bloom[plant2] <= self.bloom[plant1] and self.wilt[plant1] <= self.wilt[plant2]):
      return True
    elif (self.bloom[plant1] <= self.wilt[plant2] and self.wilt[plant2] <= self.wilt[plant1]):
      return True
    else:
      return False
  

if __name__ == '__main__':

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

  print test.getOrdering(height, bloom, wilt)