class Doublyll():
	def __init__(self):
		self.head = None
		self.data = None
		self.next = None
		self.prev = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def getPrev(self):
		return self.prev

	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newnext):
		self.next = newnext

	def setPrev(self,newprev):
		self.prev = newprev

	def isEmpty(self):
		return self.head==None

	def size(self):
		count = 0
		current  = self.head
		if current == None:
			return count
		else:
			while current != None:
				count = count+1
				current = current.getNext()
			return count

	def insertatbeg(self,item):
		current = self.head
		temp = Doublyll()
		temp.setData(item)
		if current == None:
			self.head = temp
		else:
			temp.setNext(current)
			current.setPrev(temp)
			self.head = temp

	def insertatend(self,item):
		current = self.head
		temp = Doublyll()
		temp.setData(item)
		while current.getNext() != None:
			current = current.getNext()
		current.setNext(temp)
		temp.setPrev(current)

	def insertatpos(self,item,pos=0):
		current = self.head
		temp = Doublyll()
		temp.setData(item)
		if pos == 0:
			self.insertatbeg(item)
		elif pos== self.size()+1:
			self.insertatend(item)
		else:
			i=0
			while(i<pos):
				current = current.getNext()
				i=i+1
			temp.setNext(current.getNext())
			temp.setPrev(current)

	def showlist(self):
		current = self.head
		if current == None:
			print "Empty list"
		elif current.getNext() is None:
			print current.getData()
		else:
			while current != None:
				print current.getData()
				current = current.getNext()
dl = Doublyll()
dl.insertatbeg(55)
dl.insertatbeg(85)
dl.insertatbeg(75)
dl.insertatend(105)
dl.insertatend(155)
dl.insertatpos(188,2)
dl.showlist()