"""
Implement a MyQueue class which implements a queue
using two stacks.
"""

class MyQueue:
	def __init__(self):
		s1=Stack()
		s2=Stack()
		self.set = [s1,s2]

	def enqueue(self,item):
		self.set[0].push(item)


	def dequeue(self):
		while self.set[0].size() != 1:
			popped_item = self.set[0].pop()
			self.set[1].push(popped_item)
			if self.set[0].size() == 1:
				break
		final_element = self.set[0].pop()
		while self.set[1].isEmpty() == False:
			self.set[0].push(self.set[1].pop())
			#popped_item = self.set[1].pop()
			#self.set[0].push(popped_item)
		return final_element



class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		#self.items.append(item)
		self.items.insert(0,item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

q1=MyQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
print(q1.dequeue())
print(q1.dequeue())





