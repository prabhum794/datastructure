class Node():
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

	def showlist(self):
		current = self.head
		if current == None:
			print "Empty List"
		else:
			while current != None:
				print current.getData()
				current = current.getNext()

	def size(self):
		current = self.head
		count = 0
		while current != None:
			current = current.getNext()
			count = count+1
		return count

	def search(self,sitem):
		current = self.head
		found = False
		while current != None and found is not True:
			if current.getData() == sitem:
				found = True
			else:
				current = current.getNext()
		return found

	def insertatbeg(self,data):
		temp = Node()
		temp.setData(data)
		temp.setNext(self.head)
		self.head = temp

	def insertatend(self,data):
		temp = Node()
		temp.setData(data)
		current = self.head
		while current.getNext() != None:
			current = current.getNext()
		current.setNext(temp)

	def insertatpos(self,data,pos=0):
		if pos==0:
			self.insertatbeg(data)
		elif pos==self.size()+1:
			print pos,self.size()
			self.insertatend(data)
		else:
			temp = Node()
			temp.setData(data)
			current = self.head
			i = 2
			while(i<pos):
				current = current.getNext()
				i=i+1
			temp.setNext(current.getNext())
			current.setNext(temp)


n = Node()
n.insertatpos(55)
n.insertatpos(88)
n.insertatpos(99)
n.insertatpos(100)
n.insertatpos(200)
n.insertatpos(300)
n.insertatpos(990,3)
n.insertatpos(1400,8)
n.showlist()
	

	



