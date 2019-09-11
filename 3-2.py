"""
How would you design a stack , in addition to push and pop, has a 
function min which returns the minimum element? push, pop, and min
should all operate in O(1) time.
"""

class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

	def minElement(self):
		if len(self.items) > 0:
			result = self.items[0]
		for items in self.items:
			if items < result:
				result = items
		return result

s=Stack()
s.push(1342)
s.push(234123)
s.push(5)
print(s.minElement())

"""
s=Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())
"""