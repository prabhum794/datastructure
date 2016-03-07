class CQueue():
	def __init__(self):
		self.head = None
		self.data = None
		self.next = None

	def getNext(self):
		return self.next

	def setData(self,newdata):
		self.data = newdata

	def getData(self):
		return self.data

	def setNext(self,newnext):
		self.next = newnext

	def isEmpty(self):
		return self.head==None

	def size(self):

	def printqueue(self):

	def enqueue(self,data):

	def dequeue(self):
		

cq = CQueue(25)
cq.add(50)
cq.add(60)

print cq.printqueue()

