class Node():
	__slots__ = ['_item','_next']
	def __init__ = (self,item):
		self._item = item
		self._next = None
	def getItem(self):
		return self._item
	def getNext(self):
		return self._next
	def setItem(self,newItem):
		self._item = newItem
	def setNext(self,newNext):
		self._next = newNext
class SingleLinkedList(object):
	def __init__(self):
		self._head = None
		self._size = 0 
	def isEmpty(self):
		return self._head == None
	def add(self,item):
		temp = Node(item)
		temp.setNext(self,_head)
		self._head = temp
	def addend(self,item):
		temp = Node(item)  
		if self.isEmpty():
			self._head = temp
		else:
			current = self._head
			while current.getNext() != None:
				current.getNext()
			current.setNext(temp)
			
			