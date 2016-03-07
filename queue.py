class Queue():
	def __init__(self):
		self.items = []

	def enqueue(self,data):
		self.items.insert(0,data)

	def dequeue(self):
		return self.items.pop()

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

q = Queue()
q.enqueue(22)
q.enqueue(21)
print q.dequeue()
print q.isEmpty()