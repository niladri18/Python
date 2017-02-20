import sys

class Node:
	def __init__(self):
		self.data = []
		self.child = {}
		self.label = False # End of word
	def getdata(self):
		return self.data
		
	def isEmpty(self):
		flag = (self.data == []) and (self.child == {}) and (self.label == False)
		return flag
		
	def isleaf(self):
		return self.label
		
	def addfirst(self,word):
		print('first',word)
		n = len(word)
		i = 0
		current = self
		while i < n:
			current.data = [word[i]]
			current.child[word[i]] = Node()
			current = current.child[word[i]]
			i += 1
		current.label = True
	
	def add(self,word):
		n = len(word)
		i = 0
		current = self
		while i < n:
			if word[i] not in current.data:
				current.data.append(word[i])
				current.child[word[i]] = Node()
				current = current.child[word[i]]
			else:
				current = current.child[word[i]]
			i += 1
		current.label = True	

	def prefixnode(self,word):
		n = len(word)
		current = self
		flag = True
		i = 0
		while i < n and flag:
			if word[i] in current.data:
				current = current.child[word[i]]
				i += 1
			else:
				flag = False
				return -1
		a = list(current.countnode(0))		
		print(len(a))		
				
	def countnode(self,num):
		if self.label:
			yield(num) 
			for node in self.child.values():
				if not node.isEmpty():
					num += 1
					yield from node.countnode(num)
					num -= 1
		if not self.label:
			for node in self.child.values():
				if not node.isEmpty():
					num += 1
					yield from node.countnode(num)
					num -= 1			
					
		
	def printnode(self,xp):
		if self.label:
			#print(*xp,sep = '')
			yield (''.join(xp))
			for i,node in self.child.items():
				if not node.isEmpty(): 
					xp.append(i)
					yield from node.printnode(xp)
					xp.pop()
		else:
			for i,node in self.child.items():
				if not node.isEmpty():
					xp.append(i)
					yield from node.printnode(xp)
					xp.pop()

class Trie:
	def __init__(self):
		self.item = None
		
	def insert(self,word):
		word = word.strip()
		if self.item == None:
			self.item = Node()
			return self.item.addfirst(word)
		else:
			return self.item.add(word)
	def prefix(self,word):
		return self.item.prefixnode(word)
	def count(self):
		return self.item.countnode(0)
	def printword(self):
		xp = []
		return self.item.printnode(xp)
			
			
