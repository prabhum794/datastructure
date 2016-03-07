class Dequeue():
	def __init__(self):
		self.items = []

	def enqfront(self,item):
		self.items.insert(0,item)

	def enqback(self,item):
		self.items.append(item)

	def deqfront(self):
		self.items.pop(0)

	def deqback(self):
		self.items.pop()

	def isEmpty(self):
		return len(self.items) == 0

	def showdequeue(self):
		print self.items
dq = Dequeue()
print dq.isEmpty()
dq.enqfront(25)
dq.enqfront(45)
print dq.isEmpty()
dq.showdequeue()
dq.enqback(99)
dq.showdequeue()
dq.deqback()
dq.showdequeue()
dq.enqfront('hello')
dq.showdequeue()
dq.deqfront()
dq.showdequeue()