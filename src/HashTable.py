'''

Hash Table Test

'''

class KeyValue:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def Print(self):
		print self.key, self.value

class HashTable:
	def __init__(self, size = 20):
		self.size = size
		self.data = [0] * self.size
		for i in range(self.size):
			self.data[i] = [KeyValue(0,0)]

	def getIndex(self, key):
		total = 0
		for c in key:
			total += ord(c)
		return total % self.size

	def set(self, key, value):
		index = self.getIndex(key)
		for item in self.data[index]:
			if item.key == key:
				item.value = value
				break
			elif item.key == 0:
				item.key = key
				item.value = value
				break
		else:
			self.data[index].append(KeyValue(key, value))

	def get(self, key):
		index = self.getIndex(key)
		for item in self.data[index]:
			if item.key == key:
				return item.value
		else:
			return None

	def remove(self, key):
		index = self.getIndex(key)
		for item in self.data[index]:
			if item.key == key:
				self.data[index].remove(item)
				break

	def Print(self):
		print "\nStarting to print ---------------"
		for bucket in self.data:
			print "Next Bucket"
			for keyValue in bucket:
				keyValue.Print()
		print "Print Complete ------------------"

if __name__ == '__main__':
	hashTable= HashTable()
	hashTable.set("hello","hola")
	hashTable.set("helol", "jokes")
	hashTable.set("Yippee", "Wunderbar")
	print hashTable.get("hello")
	print hashTable.get("helol")
	print hashTable.get("yo")
	print hashTable.get("Yippee")
	hashTable.Print()
	print hashTable.get("helol")
	hashTable.remove("helol")
	print hashTable.get("helol")
	hashTable.Print()