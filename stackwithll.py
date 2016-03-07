class Stack():
	def __init__(self):
		self.head = None
		self.data = None
		self.next = None

	def setNext(self,newnext):
		self.next = newnext

	def getNext(self):
		return self.next

	def getData(self):
		return self.data

	def setData(self,newdata):
		self.data = newdata

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count = count +1 
			current = current.getNext()
		return count

	def push(self,data):
		temp = Stack()
		temp.setData(data)
		temp.setNext(self.head)
		self.head = temp
	
	def search(self,sdata):
		current = self.head
		found = False
		while current != None and found is not True:
			if current.getData() == sdata:
				found = True
			else:
				current = current.getNext()
		return found

	def pop(self):
		current = self.head
		self.head = current.getNext()
		return current.getData()


	def printstack(self):
		current = self.head
		while current != None:
			print current.getData()
			current = current.getNext()

s = Stack()
s.push(20)
s.push(25)
s.push(26)
s.push(99)
s.push(105)
s.push(200)
s.push(205)
s.printstack()
print "\n"
print s.pop()
print s.pop()
print s.size()
print s.search(25)
