class Stack():
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return len(self.items) == 0

	def push(self,data):
		self.items.append(data)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)


s1 = Stack()
s1.push(25)
s1.push(27)
print s1.pop()
print s1.peek()
print s1.isEmpty()