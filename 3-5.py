"""
Sort Stack: write a program to sort a stack such that the smallest items are on the top.
You can use additional temporary stack, but you may not copy the elements into ay other data 
structures (such as an array). The stack supports the following operations: push, pop, peek, and isEmpty.
"""

class twoStacks:
	def __init__(self):
		s1=Stack()
		s2=Stack()
		self.set = [s1,s2]

	def push(self,item):
		self.set[0].push(item)

	def pop(self):
		return self.set[0].pop()

	def sort(self):
		counter = self.set[0].size()
		#print(counter)
		while counter != 0:
			if counter == 0:
				break
			maxval = 0
			for i in range(counter):
				var = self.set[0].pop()
				if var > maxval:
					maxval = var
				self.set[1].push(var)
			self.set[0].push(maxval)
			#print(maxval)
			for i in range(counter):
				var = self.set[1].pop()
				if var == maxval:
					None
				if var != maxval:
					self.set[0].push(var)
			counter -= 1


class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)
		#self.items.insert(0,item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

stacks=twoStacks()
stacks.push(4)
stacks.push(2)
stacks.push(1)
stacks.push(400)
stacks.push(9)
stacks.sort()
print("done sorting")
print(stacks.pop())
print(stacks.pop())
print(stacks.pop())
print(stacks.pop())
print(stacks.pop())
