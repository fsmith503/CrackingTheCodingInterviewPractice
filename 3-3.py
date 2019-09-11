"""
Imagine a literal stack of plates. if the stack gets too high, it might topples.
Therefore in real life, we would likely state a new stack when the pervious stack exceeds some
threshold.
Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several 
stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push and
SetOfStacks.pop() should behave identically to a single stack that is, pop() should return the same 
values as it would if there were just a single stack.
"""


class SetOfStacks:
	def __init__(self):
		s1=Stack()
		self.set = [s1]

	def push(self, item):
		for stacks in self.set:
			if stacks.size() < 6:
				stacks.push(item)
			if stacks.size() == 5:
				s2=Stack()
				self.set.append(s2)
				self.set[len(self.set)-1].push(item)
				print("new stack made")
				#print(item)
				break
				

	def pop(self):
		a = len(self.set)
		for i in range(len(self.set),0,-1):
			if self.set[i-1].isEmpty == True:
				None
			else:
				return self.set[i-1].pop()

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

set1=SetOfStacks()
set1.push(1)
set1.push(2)
set1.push(3)
set1.push(4)
set1.push(5) #stack
set1.push(6)
set1.push(7)
set1.push(8)
set1.push(9)
set1.push(10) #stack
set1.push(11)
set1.push(12)
print(set1.pop())
print(set1.pop())
print(set1.pop())


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
