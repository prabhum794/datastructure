class Queue():
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

	def enqueue(self,data):
		if self.head == None:
			temp = Queue()
			temp.setData(data)
			self.head = temp
		else:
			current = self.head
			temp = Queue()
			temp.setData(data)
			temp.setNext(current)
			self.head = temp

	def dequeue(self):
		current = self.head
		if current == None:
			print "Empty Queue"
		else:
			currentnext = current.getNext()
			if currentnext == None:
				current.setNext(None)
			else:
				while currentnext.getNext() != None:
					current = current.getNext()
					currentnext = currentnext.getNext()
				current.setNext(None)
				return current.getData()

	
	def printqueue(self):
		current = self.head
		while current != None:
			print current.getData()
			current = current.getNext()		

q = Queue()
q.enqueue(25)
q.enqueue(26)
q.enqueue(27)
q.enqueue(28)
q.enqueue(10)
print q.dequeue()
print q.size()






