

# CTCI 2.1
import math

from random import randint

class Node(object):
    #Constructor
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class LinkedList(object):
    #Constructor
    def __init__(self, head = None, size = None):
        self.head = head
        self.size = size

    #Display
    def __str__(self):
        res = []
        cur = self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return ' -> '.join(res)



    #Insert
    def insert_head(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            temp = Node(val) #temp Node
            temp.next = self.head  #Head
            self.head = temp #headreferenceTemp Node

    #nsert
    def insert_tail(self, val):
        if self.head == None:
            self.head = Node(val)
        else:
            cur = self.head
            temp = Node(val)
            while cur.next:  #idk
                cur = cur.next
            cur.next = temp

    #Generate Insert 10
    def generate(self):
        for _ in xrange(10):
            self.insert_tail(randint(0,9))

    #Insert
    def insert_multiple(self, val):
        for v in val:
            self.insert_tail(v)

    #Search
    def search(self, val):
        if self.head == None:
            raise ValueError("List is empty")

        cur = self.head
        while cur:
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    #Delete V1 using Prev
    def delete_1(self, val):
        if self.head == None:
            return self.head

        cur = self.head
        prev = None

        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
            prev = cur
            cur = cur.next

    #Delete V2 not using Prev
    def delete_2(self, val):
        if self.head == None:
            return self.head

        cur = self.head
        #Edge case
        if cur.val == val:
            self.head = cur.next

        #The rest
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

def remove_dups(ll, prev=None):
    head = ll.head
    cur = ll.head
    hash = {}

    while cur:
        if cur.val in hash:
            prev.next = cur.next
        else:
            hash[cur.val] = 1
        prev = cur
        cur = cur.next
    return head


# 2 Pointers (Runner Methods)
# Space complexity: O(1)
# Time complexity: O(N^2)
def count_func(ll):
    head = ll.head
    cur = ll.head
    runner = ll.head
    count = 0
    while cur:
        prev = runner
        runner = runner.next
        if runner == None:
            count += 1
            cur = cur.next
            runner = cur
    return count

def delete_mid_node(ll,k):
    head = ll.head
    cur = ll.head
    runner = ll.head
    count = 0

    while cur:
        prev = runner
        runner = runner.next

        if runner and count == k:
           prev.next = runner.next
           runner = runner.next
           return head

        if runner == None:
            count += 1
            cur = cur.next
            runner = cur
    return head



#Some Tests:
ll = LinkedList()
ll.generate()
#print(ll)

len_count = count_func(ll)
mid_index = math.floor(len_count/2)
print(len_count)
print(ll)
delete_mid_node(ll, mid_index-1)
print(ll)

