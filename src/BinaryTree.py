'''

Binary Tree

'''

class BinaryTreeNode:
	def __init__(self, name, leftNode, rightNode):
		self.name = name
		self.leftNode = leftNode
		self.rightNode = rightNode

	def PreOrderTraverse(self):
		order = [self.name]
		if self.leftNode:
			order += self.leftNode.PreOrderTraverse()
		if self.rightNode:
			order += self.rightNode.PreOrderTraverse()
		return order

	def InOrderTraverse(self):
		order = []
		if self.leftNode:
			order += self.leftNode.InOrderTraverse()
		order += [self.name]
		if self.rightNode:
			order += self.rightNode.InOrderTraverse()
		return order

	def PostOrderTraverse(self):
		order = []
		if self.leftNode:
			order += self.leftNode.PostOrderTraverse()
		if self.rightNode:
			order += self.rightNode.PostOrderTraverse()
		order += [self.name]
		return order

	def TreeHeight(self):
		lHeight, rHeight = 0, 0
		if self.leftNode:
			lHeight = self.leftNode.TreeHeight()
		if self.rightNode:
			rHeight = self.rightNode.TreeHeight()
		if lHeight > rHeight:
			return lHeight + 1
		else:
			return rHeight + 1

	def BalanceFactor(self):
		lHeight, rHeight = 0, 0
		if self.leftNode:
			self.leftNode.BalanceFactor()
			lHeight = self.leftNode.TreeHeight()
		if self.rightNode:
			rHeight = self.rightNode.TreeHeight()
		print "Node", self.name, "Has Balance", lHeight - rHeight
		if self.rightNode:
			self.rightNode.BalanceFactor()

class BinaryTree:
	def __init__(self, root):
		self.root = root

	def PreOrderTraverse(self):
		return self.root.PreOrderTraverse()

	def InOrderTraverse(self):
		return self.root.InOrderTraverse()

	def PostOrderTraverse(self):
		return self.root.PostOrderTraverse()

	def TreeHeight(self):
		return self.root.TreeHeight()

	def BalanceFactor(self):
		self.root.BalanceFactor() 

'''
		|--	7---------------|
	|--	1---|			|--	9---|
	0 	|---3---|		8		10
		2	|---5---|
			4		6

'''

node4 = BinaryTreeNode(4, None, None)
node6 = BinaryTreeNode(6, None, None)
node2 = BinaryTreeNode(2, None, None)
node5 = BinaryTreeNode(5, node4, node6)
node0 = BinaryTreeNode(0, None, None)
node3 = BinaryTreeNode(3, node2, node5)
node8 = BinaryTreeNode(8, None, None)
node10 = BinaryTreeNode(10, None, None)
node1 = BinaryTreeNode(1, node0, node3)
node9 = BinaryTreeNode(9, node8, node10)
node7 = BinaryTreeNode(7, node1, node9)

binaryTree = BinaryTree(node7)

print binaryTree.PreOrderTraverse()

print binaryTree.InOrderTraverse()

print binaryTree.PostOrderTraverse()

print binaryTree.TreeHeight()

print binaryTree.BalanceFactor()